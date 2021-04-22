from typing import Dict

from checkov.common.models.enums import CheckCategories, CheckResult
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck


class DatadogJavaLambdaVersion(BaseResourceCheck):
    def __init__(self) -> None:
        name = """
        Ensure Java Lambda functions use the correct runtime version (https://confluence.alpiq.com/datadog-lambda-setup)
            runtime = "java11" | "java8.al2"
        """
        id = "CKV_DD_001"
        supported_resources = ["aws_lambda_function"]
        categories = [CheckCategories.CONVENTION]
        super().__init__(
            name=name,
            id=id,
            categories=categories,
            supported_resources=supported_resources,
        )

    def scan_resource_conf(self, conf: Dict) -> CheckResult:
        runtime = conf.get("runtime", [""])[0]

        if runtime.startswith("java"):
            if runtime in ["java11", "java8.al2"]:
                return CheckResult.PASSED

            return CheckResult.FAILED

        return CheckResult.UNKNOWN


check = DatadogJavaLambdaVersion()
