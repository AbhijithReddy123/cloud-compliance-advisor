from fastapi import FastAPI
from services.aws import get_ec2_instances
from utils.validators import check_ec2_compliance
import yaml

app = FastAPI()

@app.get("/check/aws/ec2")
def ec2_check():
    with open("rules/config.yaml", "r") as f:
        config = yaml.safe_load(f)

    instances = get_ec2_instances()
    results = check_ec2_compliance(instances, config["aws"]["ec2"])
    return {"results": results}
