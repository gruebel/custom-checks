from typing import Dict

from checkov.common.models.enums import CheckCategories, CheckResult
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck


class DatadogJavaLambdaEnvVars(BaseResourceCheck):
    def __init__(self) -> None:
        name = """
        Ensure Java Lambda functions have the correct env vars set (https://confluence.alpiq.com/datadog-lambda-setup)
            JAVA_TOOL_OPTIONS    = "-javaagent:\"/opt/java/lib/dd-java-agent.jar\""
            DD_JMXFETCH_ENABLED  = "false"
            DD_LOGS_INJECTION    = "true"
            DD_MERGE_XRAY_TRACES = "true"
            DD_TRACE_ENABLED     = "true"
        """
        id = "CKV_DD_002"
        supported_resources = ["aws_lambda_function"]
        categories = [CheckCategories.CONVENTION]
        super().__init__(
            name=name,
            id=id,
            categories=categories,
            supported_resources=supported_resources,
        )

    def scan_resource_conf(self, conf: Dict) -> CheckResult:
        if conf.get("runtime", [""])[0].startswith("java"):

            if "environment" in conf.keys() and "variables" in conf["environment"][0]:
                env_vars = conf["environment"][0]["variables"][0]

                if env_vars.get("JAVA_TOOL_OPTIONS") != "-javaagent:\\\"/opt/java/lib/dd-java-agent.jar\\\"":
                    return CheckResult.FAILED
                if env_vars.get("DD_JMXFETCH_ENABLED") != "false":
                    return CheckResult.FAILED
                if env_vars.get("DD_LOGS_INJECTION") != "true":
                    return CheckResult.FAILED
                if env_vars.get("DD_MERGE_XRAY_TRACES") != "true":
                    return CheckResult.FAILED
                if env_vars.get("DD_TRACE_ENABLED") != "true":
                    return CheckResult.FAILED

                return CheckResult.PASSED

            return CheckResult.FAILED

        return CheckResult.UNKNOWN


check = DatadogJavaLambdaEnvVars()
