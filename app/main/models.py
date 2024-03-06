from django.db import models

# Create your models here.
class PredictApi(models.Model):


    STATE_CHOICES = [
        ("", "Choose State"),
        ("AL", "Alabama"),
        ("AK", "Alaska"),
        ("AZ", "Arizona"),
        ("AR", "Arkansas"),
        ("CA", "Californie"),
        ("CO", "Colorado"),
        ("CT", "Connecticut"),
        ("DE", "Delaware"),
        ("FL", "Floride"),
        ("GA", "Géorgie"),
        ("HI", "Hawaï"),
        ("ID", "Idaho"),
        ("IL", "Illinois"),
        ("IN", "Indiana"),
        ("IA", "Iowa"),
        ("KS", "Kansas"),
        ("KY", "Kentucky"),
        ("LA", "Louisiane"),
        ("ME", "Maine"),
        ("MD", "Maryland"),
        ("MA", "Massachusetts"),
        ("MI", "Michigan"),
        ("MN", "Minnesota"),
        ("MS", "Mississippi"),
        ("MO", "Missouri"),
        ("MT", "Montana"),
        ("NE", "Nebraska"),
        ("NV", "Nevada"),
        ("NH", "New Hampshire"),
        ("NJ", "New Jersey"),
        ("NM", "Nouveau Mexique"),
        ("NY", "New York"),
        ("NC", "Caroline du Nord"),
        ("ND", "Dakota du Nord"),
        ("OH", "Ohio"),
        ("OK", "Oklahoma"),
        ("OR", "Oregon"),
        ("PA", "Pennsylvanie"),
        ("RI", "Rhode Island"),
        ("SC", "Caroline du Sud"),
        ("SD", "Dakota du Sud"),
        ("TN", "Tennessee"),
        ("TX", "Texas"),
        ("UT", "Utah"),
        ("VT", "Vermont"),
        ("VA", "Virginie"),
        ("WA", "Washington"),
        ("WV", "Virginie Occidentale"),
        ("WI", "Wisconsin"),
        ("WY", "Wyoming"),
    ]


    State = models.CharField(('State'), choices=STATE_CHOICES, max_length=2, null=False, blank=False)
    Zip = models.IntegerField()
    BankState = models.CharField(('BankState'), choices=STATE_CHOICES, max_length=2, null=False, blank=False)
    ApprovalFY = models.IntegerField()
    Term = models.IntegerField()
    GrAppv = models.IntegerField()
    SBA_Appv = models.IntegerField()


