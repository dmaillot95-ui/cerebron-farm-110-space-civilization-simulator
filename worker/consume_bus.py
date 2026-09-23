import json,hashlib,pathlib
src=109; dst=110; inbox=pathlib.Path("bus/inbox/F109-to-F110-canary.json")
p=json.loads(inbox.read_text());assert p["source"]==src and p["destination"]==dst and p["cycle_id"]=="SPACE-BUS-DELIVERY-0001"
input_fingerprint=hashlib.sha256(json.dumps(p,sort_keys=True,separators=(",",":")).encode()).hexdigest()
out={"schema_version":"SPACE_CONSUMER_V1","cycle_id":p["cycle_id"],"producer":dst,"consumed_source":src,"input_fingerprint":input_fingerprint,"derived_value":p["payload"]["value"]+dst,"status":"PASS","epistemic":"REAL_CROSS_REPO_PACKET_CONSUMPTION_CANARY_NOT_PHYSICAL_MODEL"}
out["outputs_sha"]=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(",",":")).encode()).hexdigest();pathlib.Path("artifacts").mkdir(exist_ok=True);pathlib.Path("artifacts/consumed.json").write_text(json.dumps(out,indent=2)+"\\n");print(json.dumps(out))
