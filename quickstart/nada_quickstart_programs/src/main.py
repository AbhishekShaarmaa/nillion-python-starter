from nada_dsl import *

def nada_main():
    business = Party(name="Business")
    auditor = Party(name="Auditor")
    
    financial_health = SecretInteger(Input(name="financial_health", party=business))
    compliance = SecretInteger(Input(name="compliance", party=business))
    operational_efficiency = SecretInteger(Input(name="operational_efficiency", party=business))
    risk_management = SecretInteger(Input(name="risk_management", party=business))

    weight_financial_health = SecretInteger(Input(name="weight_financial_health", party=auditor))
    weight_compliance = SecretInteger(Input(name="weight_compliance", party=auditor))
    weight_operational_efficiency = SecretInteger(Input(name="weight_operational_efficiency", party=auditor))
    weight_risk_management = SecretInteger(Input(name="weight_risk_management", party=auditor))

    total_weighted_score = (financial_health * weight_financial_health +
                            compliance * weight_compliance +
                            operational_efficiency * weight_operational_efficiency +
                            risk_management * weight_risk_management)

    total_weight = weight_financial_health + weight_compliance + weight_operational_efficiency + weight_risk_management

    weighted_average_score = total_weighted_score / total_weight

    return [Output(weighted_average_score, "audit_score", business)]


