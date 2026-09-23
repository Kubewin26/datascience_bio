"""Day 1 Milestone: Task 4

Inspects raw clinical biopsy JSON schema using Pydantic validation contracts.
"""

import json
from pydantic import BaseModel, Field, ValidationError


# 1. Define the Strict Clinical Schema Contract
class BiopsyRecordSchema(BaseModel):
    patient_id: str
    age: int = Field(ge=0, le=120, description="Age must be between 0 and 120")
    tumor_size_mm: float = Field(gt=0, description="Tumor diameter in millimeters")
    brca1_mutation: bool
    estrogen_receptor_status: str
    lymph_nodes_positive: int = Field(ge=0)


def inspect_clinical_data(filepath: str) -> None:
    print(f"[*] Ingesting raw JSON data from: {filepath}")

    # Step 1: Open and read the raw JSON file
    with open(filepath, "r") as f:
        raw_payload = json.load(f)

    print(f"[*] Raw Payload Loaded:\n    {raw_payload}")

    # Step 2: Validate the payload against our Pydantic Contract
    try:
        validated_record = BiopsyRecordSchema(**raw_payload)
        print("\n[+] SUCCESS: Schema Integrity Verified!")
        print(f"    - Patient ID: {validated_record.patient_id}")
        print(f"    - Tumor Diameter: {validated_record.tumor_size_mm} mm")
        print(
            f"    - BRCA1 Status: {'Mutated (High Risk)' if validated_record.brca1_mutation else 'Normal'}"
        )
        print(f"    - ER Status: {validated_record.estrogen_receptor_status}")
    except ValidationError as e:
        print(f"\n[-] DATA CORRUPTION DETECTED:\n{e}")


if __name__ == "__main__":
    inspect_clinical_data("data/patient_biopsy.json")
