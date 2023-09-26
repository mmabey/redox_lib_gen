# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY gen_redox_lib. DO NOT MODIFY MANUALLY!!  ---- #

from __future__ import annotations

from typing import List, Union

from pydantic import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel


class Cancel(EventTypeAbstractModel):
    Meta_: CancelMeta = Field(..., alias="Meta")
    Patient_: CancelPatient = Field(..., alias="Patient")
    Referral_: CancelReferral = Field(None, alias="Referral")
    Visit_: CancelVisit = Field(None, alias="Visit")


class CancelMeta(RedoxAbstractModel):
    DataModel_: str = Field(..., alias="DataModel")
    Destinations_: List[CancelMetaDestination] = Field(None, alias="Destinations")
    EventDateTime_: Union[str, None] = Field(None, alias="EventDateTime")
    EventType_: str = Field(..., alias="EventType")
    FacilityCode_: Union[str, None] = Field(None, alias="FacilityCode")
    Logs_: List[CancelMetaLog] = Field(None, alias="Logs")
    Message_: CancelMetaMessage = Field(None, alias="Message")
    Source_: CancelMetaSource = Field(None, alias="Source")
    Test_: Union[bool, None] = Field(None, alias="Test")
    Transmission_: CancelMetaTransmission = Field(None, alias="Transmission")


class CancelMetaDestination(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    Name_: Union[str, None] = Field(None, alias="Name")


class CancelMetaLog(RedoxAbstractModel):
    AttemptID_: Union[str, None] = Field(None, alias="AttemptID")
    ID_: Union[str, None] = Field(None, alias="ID")


class CancelMetaMessage(RedoxAbstractModel):
    ID_: Union[float, None] = Field(None, alias="ID")


class CancelMetaSource(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    Name_: Union[str, None] = Field(None, alias="Name")


class CancelMetaTransmission(RedoxAbstractModel):
    ID_: Union[float, None] = Field(None, alias="ID")


class CancelPatient(RedoxAbstractModel):
    Contacts_: List[CancelPatientContact] = Field(None, alias="Contacts")
    Demographics_: CancelPatientDemographics = Field(None, alias="Demographics")
    Guarantor_: CancelPatientGuarantor = Field(None, alias="Guarantor")
    Identifiers_: List[CancelPatientIdentifier] = Field(..., alias="Identifiers")
    Insurances_: List[CancelPatientInsurance] = Field(None, alias="Insurances")
    Notes_: List[str] = Field(None, alias="Notes")


class CancelPatientContact(RedoxAbstractModel):
    Address_: CancelPatientContactAddress = Field(None, alias="Address")
    EmailAddresses_: List[str] = Field(None, alias="EmailAddresses")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    LastName_: Union[str, None] = Field(None, alias="LastName")
    MiddleName_: Union[str, None] = Field(None, alias="MiddleName")
    PhoneNumber_: CancelPatientContactPhoneNumber = Field(None, alias="PhoneNumber")
    RelationToPatient_: Union[str, None] = Field(None, alias="RelationToPatient")
    Roles_: List[str] = Field(None, alias="Roles")


class CancelPatientContactAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class CancelPatientContactPhoneNumber(RedoxAbstractModel):
    Home_: Union[str, None] = Field(None, alias="Home")
    Mobile_: Union[str, None] = Field(None, alias="Mobile")
    Office_: Union[str, None] = Field(None, alias="Office")


class CancelPatientDemographics(RedoxAbstractModel):
    Address_: CancelPatientDemographicsAddress = Field(None, alias="Address")
    Citizenship_: List[str] = Field(None, alias="Citizenship")
    DOB_: Union[str, None] = Field(None, alias="DOB")
    DeathDateTime_: Union[str, None] = Field(None, alias="DeathDateTime")
    EmailAddresses_: List[str] = Field(None, alias="EmailAddresses")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    IsDeceased_: Union[bool, None] = Field(None, alias="IsDeceased")
    IsHispanic_: Union[bool, None] = Field(None, alias="IsHispanic")
    Language_: Union[str, None] = Field(None, alias="Language")
    LastName_: Union[str, None] = Field(None, alias="LastName")
    MaritalStatus_: Union[str, None] = Field(None, alias="MaritalStatus")
    MiddleName_: Union[str, None] = Field(None, alias="MiddleName")
    PhoneNumber_: CancelPatientDemographicsPhoneNumber = Field(
        None, alias="PhoneNumber"
    )
    Race_: Union[str, None] = Field(None, alias="Race")
    Religion_: Union[str, None] = Field(None, alias="Religion")
    SSN_: Union[str, None] = Field(None, alias="SSN")
    Sex_: Union[str, None] = Field(None, alias="Sex")


class CancelPatientDemographicsAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class CancelPatientDemographicsPhoneNumber(RedoxAbstractModel):
    Home_: Union[str, None] = Field(None, alias="Home")
    Mobile_: Union[str, None] = Field(None, alias="Mobile")
    Office_: Union[str, None] = Field(None, alias="Office")


class CancelPatientGuarantor(RedoxAbstractModel):
    Address_: CancelPatientGuarantorAddress = Field(None, alias="Address")
    DOB_: Union[str, None] = Field(None, alias="DOB")
    EmailAddresses_: List[str] = Field(None, alias="EmailAddresses")
    Employer_: CancelPatientGuarantorEmployer = Field(None, alias="Employer")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    LastName_: Union[str, None] = Field(None, alias="LastName")
    MiddleName_: Union[str, None] = Field(None, alias="MiddleName")
    Number_: Union[str, None] = Field(None, alias="Number")
    PhoneNumber_: CancelPatientGuarantorPhoneNumber = Field(None, alias="PhoneNumber")
    RelationToPatient_: Union[str, None] = Field(None, alias="RelationToPatient")
    SSN_: Union[str, None] = Field(None, alias="SSN")
    Sex_: Union[str, None] = Field(None, alias="Sex")
    Spouse_: CancelPatientGuarantorSpouse = Field(None, alias="Spouse")
    Type_: Union[str, None] = Field(None, alias="Type")


class CancelPatientGuarantorAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class CancelPatientGuarantorEmployer(RedoxAbstractModel):
    Address_: CancelPatientGuarantorEmployerAddress = Field(None, alias="Address")
    Name_: Union[str, None] = Field(None, alias="Name")
    PhoneNumber_: Union[str, None] = Field(None, alias="PhoneNumber")


class CancelPatientGuarantorEmployerAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class CancelPatientGuarantorPhoneNumber(RedoxAbstractModel):
    Business_: Union[str, None] = Field(None, alias="Business")
    Home_: Union[str, None] = Field(None, alias="Home")
    Mobile_: Union[str, None] = Field(None, alias="Mobile")


class CancelPatientGuarantorSpouse(RedoxAbstractModel):
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    LastName_: Union[str, None] = Field(None, alias="LastName")


class CancelPatientIdentifier(RedoxAbstractModel):
    ID_: str = Field(..., alias="ID")
    IDType_: str = Field(..., alias="IDType")


class CancelPatientInsurance(RedoxAbstractModel):
    AgreementType_: Union[str, None] = Field(None, alias="AgreementType")
    Company_: CancelPatientInsuranceCompany = Field(None, alias="Company")
    CoverageType_: Union[str, None] = Field(None, alias="CoverageType")
    EffectiveDate_: Union[str, None] = Field(None, alias="EffectiveDate")
    ExpirationDate_: Union[str, None] = Field(None, alias="ExpirationDate")
    GroupName_: Union[str, None] = Field(None, alias="GroupName")
    GroupNumber_: Union[str, None] = Field(None, alias="GroupNumber")
    Insured_: CancelPatientInsuranceInsured = Field(None, alias="Insured")
    MemberNumber_: Union[str, None] = Field(None, alias="MemberNumber")
    Plan_: CancelPatientInsurancePlan = Field(None, alias="Plan")
    PolicyNumber_: Union[str, None] = Field(None, alias="PolicyNumber")
    Priority_: Union[str, None] = Field(None, alias="Priority")


class CancelPatientInsuranceCompany(RedoxAbstractModel):
    Address_: CancelPatientInsuranceCompanyAddress = Field(None, alias="Address")
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    Name_: Union[str, None] = Field(None, alias="Name")
    PhoneNumber_: Union[str, None] = Field(None, alias="PhoneNumber")


class CancelPatientInsuranceCompanyAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class CancelPatientInsuranceInsured(RedoxAbstractModel):
    Address_: CancelPatientInsuranceInsuredAddress = Field(None, alias="Address")
    DOB_: Union[str, None] = Field(None, alias="DOB")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    Identifiers_: List[CancelPatientInsuranceInsuredIdentifier] = Field(
        None, alias="Identifiers"
    )
    LastName_: Union[str, None] = Field(None, alias="LastName")
    MiddleName_: Union[str, None] = Field(None, alias="MiddleName")
    Relationship_: Union[str, None] = Field(None, alias="Relationship")
    SSN_: Union[str, None] = Field(None, alias="SSN")
    Sex_: Union[str, None] = Field(None, alias="Sex")


class CancelPatientInsuranceInsuredAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class CancelPatientInsuranceInsuredIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class CancelPatientInsurancePlan(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    Name_: Union[str, None] = Field(None, alias="Name")
    Type_: Union[str, None] = Field(None, alias="Type")


class CancelReferral(RedoxAbstractModel):
    AlternateID_: Union[str, None] = Field(None, alias="AlternateID")
    Authorization_: CancelReferralAuthorization = Field(None, alias="Authorization")
    Category_: Union[str, None] = Field(None, alias="Category")
    DateTime_: Union[str, None] = Field(None, alias="DateTime")
    DepartmentSpecialty_: Union[str, None] = Field(None, alias="DepartmentSpecialty")
    Diagnoses_: List[CancelReferralDiagnosis] = Field(None, alias="Diagnoses")
    ExpirationDateTime_: Union[str, None] = Field(None, alias="ExpirationDateTime")
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    Notes_: List[str] = Field(None, alias="Notes")
    Priority_: Union[str, None] = Field(None, alias="Priority")
    Procedures_: List[CancelReferralProcedure] = Field(None, alias="Procedures")
    ProcessDateTime_: Union[str, None] = Field(None, alias="ProcessDateTime")
    ProviderSpecialty_: Union[str, None] = Field(None, alias="ProviderSpecialty")
    Providers_: List[CancelReferralProvider] = Field(None, alias="Providers")
    Reason_: Union[str, None] = Field(None, alias="Reason")
    Status_: Union[str, None] = Field(None, alias="Status")
    Type_: Union[str, None] = Field(None, alias="Type")
    Visit_: CancelReferralVisit = Field(None, alias="Visit")


class CancelReferralAuthorization(RedoxAbstractModel):
    AuthorizedTreatmentCount_: Union[str, None] = Field(
        None, alias="AuthorizedTreatmentCount"
    )
    Company_: CancelReferralAuthorizationCompany = Field(None, alias="Company")
    DateTime_: Union[str, None] = Field(None, alias="DateTime")
    ExpirationDateTime_: Union[str, None] = Field(None, alias="ExpirationDateTime")
    Notes_: List[str] = Field(None, alias="Notes")
    Number_: Union[str, None] = Field(None, alias="Number")
    Plan_: CancelReferralAuthorizationPlan = Field(None, alias="Plan")
    ReimbursementLimit_: Union[str, None] = Field(None, alias="ReimbursementLimit")
    RequestedTreatmentCount_: Union[str, None] = Field(
        None, alias="RequestedTreatmentCount"
    )
    RequestedTreatmentUnits_: Union[str, None] = Field(
        None, alias="RequestedTreatmentUnits"
    )


class CancelReferralAuthorizationCompany(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    Name_: Union[str, None] = Field(None, alias="Name")


class CancelReferralAuthorizationPlan(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    Name_: Union[str, None] = Field(None, alias="Name")


class CancelReferralDiagnosis(RedoxAbstractModel):
    Code_: Union[str, None] = Field(None, alias="Code")
    Codeset_: Union[str, None] = Field(None, alias="Codeset")
    DocumentedDateTime_: Union[str, None] = Field(None, alias="DocumentedDateTime")
    Name_: Union[str, None] = Field(None, alias="Name")
    Notes_: List[str] = Field(None, alias="Notes")
    Type_: Union[str, None] = Field(None, alias="Type")


class CancelReferralProcedure(RedoxAbstractModel):
    Code_: Union[str, None] = Field(None, alias="Code")
    Codeset_: Union[str, None] = Field(None, alias="Codeset")
    Description_: Union[str, None] = Field(None, alias="Description")
    Modifiers_: List[str] = Field(None, alias="Modifiers")
    Notes_: List[str] = Field(None, alias="Notes")
    Quantity_: Union[str, None] = Field(None, alias="Quantity")
    Units_: Union[str, None] = Field(None, alias="Units")


class CancelReferralProvider(RedoxAbstractModel):
    Address_: CancelReferralProviderAddress = Field(None, alias="Address")
    ContactInfo_: Union[str, None] = Field(None, alias="ContactInfo")
    Credentials_: List[str] = Field(None, alias="Credentials")
    EmailAddresses_: List[str] = Field(None, alias="EmailAddresses")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    LastName_: Union[str, None] = Field(None, alias="LastName")
    Location_: CancelReferralProviderLocation = Field(None, alias="Location")
    PhoneNumber_: CancelReferralProviderPhoneNumber = Field(None, alias="PhoneNumber")
    Type_: Union[str, None] = Field(None, alias="Type")


class CancelReferralProviderAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class CancelReferralProviderLocation(RedoxAbstractModel):
    Department_: Union[str, None] = Field(None, alias="Department")
    DepartmentIdentifiers_: List[
        CancelReferralProviderLocationDepartmentIdentifier
    ] = Field(None, alias="DepartmentIdentifiers")
    Facility_: Union[str, None] = Field(None, alias="Facility")
    FacilityIdentifiers_: List[
        CancelReferralProviderLocationFacilityIdentifier
    ] = Field(None, alias="FacilityIdentifiers")
    Room_: Union[str, None] = Field(None, alias="Room")
    Type_: Union[str, None] = Field(None, alias="Type")


class CancelReferralProviderLocationDepartmentIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class CancelReferralProviderLocationFacilityIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class CancelReferralProviderPhoneNumber(RedoxAbstractModel):
    Office_: Union[str, None] = Field(None, alias="Office")


class CancelReferralVisit(RedoxAbstractModel):
    VisitNumber_: Union[str, None] = Field(None, alias="VisitNumber")


class CancelVisit(RedoxAbstractModel):
    VisitNumber_: Union[str, None] = Field(None, alias="VisitNumber")


Cancel.model_rebuild()
CancelMeta.model_rebuild()
CancelPatient.model_rebuild()
CancelPatientContact.model_rebuild()
CancelPatientDemographics.model_rebuild()
CancelPatientGuarantor.model_rebuild()
CancelPatientGuarantorEmployer.model_rebuild()
CancelPatientInsurance.model_rebuild()
CancelPatientInsuranceCompany.model_rebuild()
CancelPatientInsuranceInsured.model_rebuild()
CancelReferral.model_rebuild()
CancelReferralAuthorization.model_rebuild()
CancelReferralProvider.model_rebuild()
CancelReferralProviderLocation.model_rebuild()
