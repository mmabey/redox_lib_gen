# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY gen_redox_lib. DO NOT MODIFY MANUALLY!!  ---- #

from __future__ import annotations

from typing import List, Union

from pydantic import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel


class Transaction(EventTypeAbstractModel):
    Meta_: TransactionMeta = Field(..., alias="Meta")
    Patient_: TransactionPatient = Field(..., alias="Patient")
    Transactions_: List[TransactionTransaction] = Field(..., alias="Transactions")
    Visit_: TransactionVisit = Field(None, alias="Visit")


class TransactionMeta(RedoxAbstractModel):
    DataModel_: str = Field(..., alias="DataModel")
    Destinations_: List[TransactionMetaDestination] = Field(None, alias="Destinations")
    EventDateTime_: Union[str, None] = Field(None, alias="EventDateTime")
    EventType_: str = Field(..., alias="EventType")
    FacilityCode_: Union[str, None] = Field(None, alias="FacilityCode")
    Logs_: List[TransactionMetaLog] = Field(None, alias="Logs")
    Message_: TransactionMetaMessage = Field(None, alias="Message")
    Source_: TransactionMetaSource = Field(None, alias="Source")
    Test_: Union[bool, None] = Field(None, alias="Test")
    Transmission_: TransactionMetaTransmission = Field(None, alias="Transmission")


class TransactionMetaDestination(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    Name_: Union[str, None] = Field(None, alias="Name")


class TransactionMetaLog(RedoxAbstractModel):
    AttemptID_: Union[str, None] = Field(None, alias="AttemptID")
    ID_: Union[str, None] = Field(None, alias="ID")


class TransactionMetaMessage(RedoxAbstractModel):
    ID_: Union[float, None] = Field(None, alias="ID")


class TransactionMetaSource(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    Name_: Union[str, None] = Field(None, alias="Name")


class TransactionMetaTransmission(RedoxAbstractModel):
    ID_: Union[float, None] = Field(None, alias="ID")


class TransactionPatient(RedoxAbstractModel):
    Demographics_: TransactionPatientDemographics = Field(None, alias="Demographics")
    Identifiers_: List[TransactionPatientIdentifier] = Field(..., alias="Identifiers")
    Notes_: List[str] = Field(None, alias="Notes")


class TransactionPatientDemographics(RedoxAbstractModel):
    Address_: TransactionPatientDemographicsAddress = Field(None, alias="Address")
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
    PhoneNumber_: TransactionPatientDemographicsPhoneNumber = Field(
        None, alias="PhoneNumber"
    )
    Race_: Union[str, None] = Field(None, alias="Race")
    Religion_: Union[str, None] = Field(None, alias="Religion")
    SSN_: Union[str, None] = Field(None, alias="SSN")
    Sex_: Union[str, None] = Field(None, alias="Sex")


class TransactionPatientDemographicsAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class TransactionPatientDemographicsPhoneNumber(RedoxAbstractModel):
    Home_: Union[str, None] = Field(None, alias="Home")
    Mobile_: Union[str, None] = Field(None, alias="Mobile")
    Office_: Union[str, None] = Field(None, alias="Office")


class TransactionPatientIdentifier(RedoxAbstractModel):
    ID_: str = Field(..., alias="ID")
    IDType_: str = Field(..., alias="IDType")


class TransactionTransaction(RedoxAbstractModel):
    Chargeable_: TransactionTransactionChargeable = Field(..., alias="Chargeable")
    DateTimeOfService_: str = Field(..., alias="DateTimeOfService")
    Department_: TransactionTransactionDepartment = Field(None, alias="Department")
    Diagnoses_: List[TransactionTransactionDiagnosis] = Field(None, alias="Diagnoses")
    EndDateTime_: Union[str, None] = Field(None, alias="EndDateTime")
    ID_: str = Field(..., alias="ID")
    NDC_: TransactionTransactionNDC = Field(None, alias="NDC")
    OrderID_: Union[str, None] = Field(None, alias="OrderID")
    OrderingProviders_: List[TransactionTransactionOrderingProvider] = Field(
        None, alias="OrderingProviders"
    )
    Performers_: List[TransactionTransactionPerformer] = Field(None, alias="Performers")
    Procedure_: TransactionTransactionProcedure = Field(None, alias="Procedure")
    Type_: str = Field(..., alias="Type")


class TransactionTransactionChargeable(RedoxAbstractModel):
    Amount_: Union[float, None] = Field(None, alias="Amount")
    Code_: str = Field(..., alias="Code")
    Codeset_: Union[str, None] = Field(None, alias="Codeset")
    Description_: Union[str, None] = Field(None, alias="Description")
    Quantity_: Union[str, None] = Field(None, alias="Quantity")


class TransactionTransactionDepartment(RedoxAbstractModel):
    Code_: Union[str, None] = Field(None, alias="Code")
    Codeset_: Union[str, None] = Field(None, alias="Codeset")
    Name_: Union[str, None] = Field(None, alias="Name")


class TransactionTransactionDiagnosis(RedoxAbstractModel):
    Code_: Union[str, None] = Field(None, alias="Code")
    Codeset_: Union[str, None] = Field(None, alias="Codeset")
    DocumentedDateTime_: Union[str, None] = Field(None, alias="DocumentedDateTime")
    Name_: Union[str, None] = Field(None, alias="Name")
    Type_: Union[str, None] = Field(None, alias="Type")


class TransactionTransactionNDC(RedoxAbstractModel):
    Code_: Union[str, None] = Field(None, alias="Code")
    Description_: Union[str, None] = Field(None, alias="Description")


class TransactionTransactionOrderingProvider(RedoxAbstractModel):
    Address_: TransactionTransactionOrderingProviderAddress = Field(
        None, alias="Address"
    )
    Credentials_: List[str] = Field(None, alias="Credentials")
    EmailAddresses_: List[str] = Field(None, alias="EmailAddresses")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    LastName_: Union[str, None] = Field(None, alias="LastName")
    Location_: TransactionTransactionOrderingProviderLocation = Field(
        None, alias="Location"
    )
    PhoneNumber_: TransactionTransactionOrderingProviderPhoneNumber = Field(
        None, alias="PhoneNumber"
    )


class TransactionTransactionOrderingProviderAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class TransactionTransactionOrderingProviderLocation(RedoxAbstractModel):
    Department_: Union[str, None] = Field(None, alias="Department")
    DepartmentIdentifiers_: List[
        TransactionTransactionOrderingProviderLocationDepartmentIdentifier
    ] = Field(None, alias="DepartmentIdentifiers")
    Facility_: Union[str, None] = Field(None, alias="Facility")
    FacilityIdentifiers_: List[
        TransactionTransactionOrderingProviderLocationFacilityIdentifier
    ] = Field(None, alias="FacilityIdentifiers")
    Room_: Union[str, None] = Field(None, alias="Room")
    Type_: Union[str, None] = Field(None, alias="Type")


class TransactionTransactionOrderingProviderLocationDepartmentIdentifier(
    RedoxAbstractModel
):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class TransactionTransactionOrderingProviderLocationFacilityIdentifier(
    RedoxAbstractModel
):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class TransactionTransactionOrderingProviderPhoneNumber(RedoxAbstractModel):
    Office_: Union[str, None] = Field(None, alias="Office")


class TransactionTransactionPerformer(RedoxAbstractModel):
    Address_: TransactionTransactionPerformerAddress = Field(None, alias="Address")
    Credentials_: List[str] = Field(None, alias="Credentials")
    EmailAddresses_: List[str] = Field(None, alias="EmailAddresses")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    LastName_: Union[str, None] = Field(None, alias="LastName")
    Location_: TransactionTransactionPerformerLocation = Field(None, alias="Location")
    PhoneNumber_: TransactionTransactionPerformerPhoneNumber = Field(
        None, alias="PhoneNumber"
    )


class TransactionTransactionPerformerAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class TransactionTransactionPerformerLocation(RedoxAbstractModel):
    Department_: Union[str, None] = Field(None, alias="Department")
    DepartmentIdentifiers_: List[
        TransactionTransactionPerformerLocationDepartmentIdentifier
    ] = Field(None, alias="DepartmentIdentifiers")
    Facility_: Union[str, None] = Field(None, alias="Facility")
    FacilityIdentifiers_: List[
        TransactionTransactionPerformerLocationFacilityIdentifier
    ] = Field(None, alias="FacilityIdentifiers")
    Room_: Union[str, None] = Field(None, alias="Room")
    Type_: Union[str, None] = Field(None, alias="Type")


class TransactionTransactionPerformerLocationDepartmentIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class TransactionTransactionPerformerLocationFacilityIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class TransactionTransactionPerformerPhoneNumber(RedoxAbstractModel):
    Office_: Union[str, None] = Field(None, alias="Office")


class TransactionTransactionProcedure(RedoxAbstractModel):
    Code_: Union[str, None] = Field(None, alias="Code")
    Codeset_: Union[str, None] = Field(None, alias="Codeset")
    Description_: Union[str, None] = Field(None, alias="Description")
    Modifiers_: List[str] = Field(None, alias="Modifiers")


class TransactionVisit(RedoxAbstractModel):
    AccountNumber_: Union[str, None] = Field(None, alias="AccountNumber")
    Guarantor_: TransactionVisitGuarantor = Field(None, alias="Guarantor")
    Insurances_: List[TransactionVisitInsurance] = Field(None, alias="Insurances")
    Location_: TransactionVisitLocation = Field(None, alias="Location")
    PatientClass_: Union[str, None] = Field(None, alias="PatientClass")
    VisitDateTime_: Union[str, None] = Field(None, alias="VisitDateTime")
    VisitNumber_: Union[str, None] = Field(None, alias="VisitNumber")


class TransactionVisitGuarantor(RedoxAbstractModel):
    Address_: TransactionVisitGuarantorAddress = Field(None, alias="Address")
    DOB_: Union[str, None] = Field(None, alias="DOB")
    EmailAddresses_: List[str] = Field(None, alias="EmailAddresses")
    Employer_: TransactionVisitGuarantorEmployer = Field(None, alias="Employer")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    LastName_: Union[str, None] = Field(None, alias="LastName")
    MiddleName_: Union[str, None] = Field(None, alias="MiddleName")
    Number_: Union[str, None] = Field(None, alias="Number")
    PhoneNumber_: TransactionVisitGuarantorPhoneNumber = Field(
        None, alias="PhoneNumber"
    )
    RelationToPatient_: Union[str, None] = Field(None, alias="RelationToPatient")
    SSN_: Union[str, None] = Field(None, alias="SSN")
    Sex_: Union[str, None] = Field(None, alias="Sex")
    Spouse_: TransactionVisitGuarantorSpouse = Field(None, alias="Spouse")
    Type_: Union[str, None] = Field(None, alias="Type")


class TransactionVisitGuarantorAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class TransactionVisitGuarantorEmployer(RedoxAbstractModel):
    Address_: TransactionVisitGuarantorEmployerAddress = Field(None, alias="Address")
    Name_: Union[str, None] = Field(None, alias="Name")
    PhoneNumber_: Union[str, None] = Field(None, alias="PhoneNumber")


class TransactionVisitGuarantorEmployerAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class TransactionVisitGuarantorPhoneNumber(RedoxAbstractModel):
    Business_: Union[str, None] = Field(None, alias="Business")
    Home_: Union[str, None] = Field(None, alias="Home")
    Mobile_: Union[str, None] = Field(None, alias="Mobile")


class TransactionVisitGuarantorSpouse(RedoxAbstractModel):
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    LastName_: Union[str, None] = Field(None, alias="LastName")


class TransactionVisitInsurance(RedoxAbstractModel):
    AgreementType_: Union[str, None] = Field(None, alias="AgreementType")
    Company_: TransactionVisitInsuranceCompany = Field(None, alias="Company")
    CoverageType_: Union[str, None] = Field(None, alias="CoverageType")
    EffectiveDate_: Union[str, None] = Field(None, alias="EffectiveDate")
    ExpirationDate_: Union[str, None] = Field(None, alias="ExpirationDate")
    GroupName_: Union[str, None] = Field(None, alias="GroupName")
    GroupNumber_: Union[str, None] = Field(None, alias="GroupNumber")
    Insured_: TransactionVisitInsuranceInsured = Field(None, alias="Insured")
    MemberNumber_: Union[str, None] = Field(None, alias="MemberNumber")
    Plan_: TransactionVisitInsurancePlan = Field(None, alias="Plan")
    PolicyNumber_: Union[str, None] = Field(None, alias="PolicyNumber")
    Priority_: Union[str, None] = Field(None, alias="Priority")


class TransactionVisitInsuranceCompany(RedoxAbstractModel):
    Address_: TransactionVisitInsuranceCompanyAddress = Field(None, alias="Address")
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    Name_: Union[str, None] = Field(None, alias="Name")
    PhoneNumber_: Union[str, None] = Field(None, alias="PhoneNumber")


class TransactionVisitInsuranceCompanyAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class TransactionVisitInsuranceInsured(RedoxAbstractModel):
    Address_: TransactionVisitInsuranceInsuredAddress = Field(None, alias="Address")
    DOB_: Union[str, None] = Field(None, alias="DOB")
    FirstName_: Union[str, None] = Field(None, alias="FirstName")
    Identifiers_: List[TransactionVisitInsuranceInsuredIdentifier] = Field(
        None, alias="Identifiers"
    )
    LastName_: Union[str, None] = Field(None, alias="LastName")
    MiddleName_: Union[str, None] = Field(None, alias="MiddleName")
    Relationship_: Union[str, None] = Field(None, alias="Relationship")
    SSN_: Union[str, None] = Field(None, alias="SSN")
    Sex_: Union[str, None] = Field(None, alias="Sex")


class TransactionVisitInsuranceInsuredAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class TransactionVisitInsuranceInsuredIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class TransactionVisitInsurancePlan(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")
    Name_: Union[str, None] = Field(None, alias="Name")
    Type_: Union[str, None] = Field(None, alias="Type")


class TransactionVisitLocation(RedoxAbstractModel):
    Address_: TransactionVisitLocationAddress = Field(None, alias="Address")
    Bed_: Union[str, None] = Field(None, alias="Bed")
    Department_: Union[str, None] = Field(None, alias="Department")
    DepartmentIdentifiers_: List[TransactionVisitLocationDepartmentIdentifier] = Field(
        None, alias="DepartmentIdentifiers"
    )
    Facility_: Union[str, None] = Field(None, alias="Facility")
    FacilityIdentifiers_: List[TransactionVisitLocationFacilityIdentifier] = Field(
        None, alias="FacilityIdentifiers"
    )
    Room_: Union[str, None] = Field(None, alias="Room")
    Type_: Union[str, None] = Field(None, alias="Type")


class TransactionVisitLocationAddress(RedoxAbstractModel):
    City_: Union[str, None] = Field(None, alias="City")
    Country_: Union[str, None] = Field(None, alias="Country")
    County_: Union[str, None] = Field(None, alias="County")
    State_: Union[str, None] = Field(None, alias="State")
    StreetAddress_: Union[str, None] = Field(None, alias="StreetAddress")
    ZIP_: Union[str, None] = Field(None, alias="ZIP")


class TransactionVisitLocationDepartmentIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


class TransactionVisitLocationFacilityIdentifier(RedoxAbstractModel):
    ID_: Union[str, None] = Field(None, alias="ID")
    IDType_: Union[str, None] = Field(None, alias="IDType")


Transaction.model_rebuild()
TransactionMeta.model_rebuild()
TransactionPatient.model_rebuild()
TransactionPatientDemographics.model_rebuild()
TransactionTransaction.model_rebuild()
TransactionTransactionOrderingProvider.model_rebuild()
TransactionTransactionOrderingProviderLocation.model_rebuild()
TransactionTransactionPerformer.model_rebuild()
TransactionTransactionPerformerLocation.model_rebuild()
TransactionVisit.model_rebuild()
TransactionVisitGuarantor.model_rebuild()
TransactionVisitGuarantorEmployer.model_rebuild()
TransactionVisitInsurance.model_rebuild()
TransactionVisitInsuranceCompany.model_rebuild()
TransactionVisitInsuranceInsured.model_rebuild()
TransactionVisitLocation.model_rebuild()
