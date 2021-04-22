# pass

resource "aws_lambda_function" "java_11" {
  filename      = "lambda_function_payload.zip"
  function_name = "demo"
  role          = aws_iam_role.lambda.arn
  handler       = "demo.Handler::handleRequest"

  runtime = "java11"
}

resource "aws_lambda_function" "java_8_correto" {
  filename      = "lambda_function_payload.zip"
  function_name = "demo"
  role          = aws_iam_role.lambda.arn
  handler       = "demo.Handler::handleRequest"

  runtime = "java8.al2"
}

# failure

resource "aws_lambda_function" "java_8" {
  filename      = "lambda_function_payload.zip"
  function_name = "demo"
  role          = aws_iam_role.lambda.arn
  handler       = "demo.Handler::handleRequest"

  runtime = "java8"
}
