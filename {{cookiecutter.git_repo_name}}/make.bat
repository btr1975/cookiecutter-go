@ECHO off
REM GO-Lang Helpers
REM Author: Ben Trachtenberg
REM Version: 2023.2.14.001
REM
REM
REM Description:
REM     This is a Makefile to help in building and testing GO projects
REM
REM Notes:
REM     To see all OS/Architecture's you can build use "go tool dist list"
REM
REM     For compiling for ARM based architecture's you may require the GOARM variable
REM     see docs for more info
REM
IF "%1" == "all" (
    go fmt ./...
    go mod tidy
    go test ./... -v -coverprofile=coverage.out
    go tool cover -html=coverage.out -o coverage.html
    GOTO END
)

IF "%1" == "test" (
    go test ./... %2
    GOTO END
)

IF "%1" == "coverage" (
    go test ./... %2 -cover
    GOTO END
)

IF "%1" == "coverage-html" (
    go test ./... %2 -coverprofile=coverage.out
    go tool cover -html=coverage.out -o coverage.html
    GOTO END
)

IF "%1" == "format" (
    go fmt ./...
    GOTO END
)

IF "%1" == "tidy" (
    go mod tidy
    GOTO END
)

:END
