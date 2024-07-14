from pydantic import BaseModel

class Subtype(BaseModel):
    ValueInteger: int | None
    ValueMap: dict | None
    ValueString: str

class SegmentAttributes(BaseModel):
    connect: Subtype = Subtype()

class CustomerEndpoint(BaseModel):
    Address: str
    Type: str

class MediaStreams(BaseModel):
    Customer: dict

class CustomerEndpoint(BaseModel):
    Address: str
    Type: str

class MediaStreams(BaseModel):
    Customer: dict

class ContactData(BaseModel):
    Attributes: dict
    AwsRegion: str
    Channel: str
    ContactId: str
    CustomerEndpoint: CustomerEndpoint
    CustomerId: str | None
    Description: str | None
    InitialContactId: str
    InitiationMethod: str
    InstanceARN: str
    LanguageCode: str
    MediaStreams: MediaStreams
    Name: str | None
    PreviousContactId: str
    Queue: str | None
    References: dict
    RelatedContactId: str | None
    SegmentAttributes: SegmentAttributes
    SystemEndpoint: CustomerEndpoint
    Tags: dict

class Parameters(BaseModel):
    eventHandler: str

class ContactFlowEvent(BaseModel):
    Name: str
    Details: ContactData
    Parameters: Parameters
