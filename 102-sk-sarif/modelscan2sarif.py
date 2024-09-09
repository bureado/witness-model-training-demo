import sys
import json

# Conversion to SARIF format
def json_to_sarif(json_data):
    # Base SARIF structure
    sarif_output = {
        "version": "2.1.0",
        "runs": [
            {
                "tool": {
                    "driver": {
                        "name": "ModelScan",
                        "version": json_data["summary"]["modelscan_version"],
                        "informationUri": "https://modelscan.example.com",  # Example URI, update as necessary
                        "rules": []
                    }
                },
                "results": [],
                "invocations": [
                    {
                        "executionSuccessful": True,
                        "startTimeUtc": json_data["summary"]["timestamp"]
                    }
                ]
            }
        ]
    }

    # Processing the issues
    for issue in json_data["issues"]:
        rule_id = issue["scanner"]
        severity = issue["severity"].lower()
        file_path = json_data["summary"]["absolute_path"] + "/" + issue["source"]

        # Add the rule to the tool driver
        sarif_output["runs"][0]["tool"]["driver"]["rules"].append({
            "id": rule_id,
            "shortDescription": {
                "text": issue["description"]
            },
            "fullDescription": {
                "text": issue["description"]
            },
            "defaultConfiguration": {
                "level": severity
            }
        })

        # Add the issue result
        sarif_output["runs"][0]["results"].append({
            "ruleId": rule_id,
            "level": severity,
            "message": {
                "text": issue["description"]
            },
            "locations": [
                {
                    "physicalLocation": {
                        "artifactLocation": {
                            "uri": file_path
                        },
                        "region": {
                            "startLine": 1,  # Assuming line 1
                            "startColumn": 1  # Assuming column 1
                        }
                    }
                }
            ]
        })

    return sarif_output


def main():
    # Read JSON from stdin
    json_input = json.load(sys.stdin)

    # Convert JSON to SARIF
    sarif_data = json_to_sarif(json_input)

    # Output SARIF to stdout
    json.dump(sarif_data, sys.stdout, indent=4)


if __name__ == "__main__":
    main()
