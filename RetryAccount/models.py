from django.db import models
from django.contrib.auth.models import User,PermissionsMixin
from django.contrib.auth import get_user_model
from multiselectfield import MultiSelectField
User_o = get_user_model()
import PIL
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.
Interest_choice = [
('Gaming','Gaming'),
('Blogging','Blogging'),
('Sports','Sports'),
('Art & Design','Art & Design'),
('Traveling','Traveling'),
('Cooking','Cooking'),
('Music','Music'),
('Reading','Reading'),
('Collecting','Collecting'),
('Painting','Painting'),
('Dancing','Dancing'),
('Computer','Computer'),
('Animal Care','Animal Care'),
('Gardening','Gardening'),
('Yoga','Yoga'),
('Computer Programming','Computer Programming'),
('Mathematics','Mathematics'),
('Teaching','Teaching'),
('Adventure','Adventure'),
('Shopping','Shopping'),
('Photography','Photography'),
('Movie','Movie'),
]

Age_range = [
('below 15','Below 15'),
('15-20','15-20'),
('21-25','21-25'),
('26-30','26-30'),
('31-35','31-35'),
('36-40','36-40'),
('Above 40','Above 40'),
]

Gender = [
('male','male'),
('female','female'),
('other','other'),
]

Profession_choice = [
('Professions','Professions'),
('Teacher','Teacher'),
('Physician','Physician'),
('Technician','Technician'),
('Engineer','Engineer'),
('Lawyer','Lawyer'),
('Accountant','Accountant'),
('Architect','Architect'),
('Electrician','Electrician'),
('Veterinarian','Veterinarian'),
('Software Developer','Software Developer'),
('Pharmacist','Pharmacist'),
('Surveyor','Surveyor'),
('Dietitian','Dietitian'),
('Plumber','Plumber'),
('Consultant','Consultant'),
('Hairdresser','Hairdresser'),
('Chef','Chef'),
('Technologist','Technologist'),
('Mechanic','Mechanic'),
('Police officer','Police officer'),
('Dental hygienist','Dental hygienist'),
('Radiographer','Radiographer'),
('Actuary','Actuary'),
('Artist','Artist'),
('Waiting staff','Waiting staff'),
('Biomedical Engineer','Biomedical Engineer'),
('Firefighter','Firefighter'),
('Actor','Actor'),
('Surgeon','Surgeon'),
('Designer','Designer'),
('Broker','Broker'),
('Labourer','Labourer'),
('Scientist','Scientist'),
('Secretary','Secretary'),
('Librarian','Librarian'),
('Aviator','Aviator'),
('Estate agent','Estate agent'),
('Barber','Barber'),
('Physiotherapist','Physiotherapist'),
('Dentist','Dentist'),
('Athlete','Athlete'),
('Judge','Judge'),
('Tour guide','Tour guide'),
('Midwife','Midwife'),
('Paramedic','Paramedic'),
('Machinist','Machinist'),
('Health professional','Health professional'),
('Optician','Optician'),
('Butcher','Butcher'),
('Tradesman','Tradesman'),
('Operator','Operator'),
]

State_Choice = [
('Andaman and Nicobar Islands','Andaman and Nicobar Islands'),
('Andhra Pradesh','Andhra Pradesh'),
('Arunachal Pradesh','Arunachal Pradesh'),
('Assam','Assam'),
('Bihar','Bihar'),
('Chandigarh','Chandigarh'),
('Chhattisgarh','Chhattisgarh'),
('Dadra and Nagar Haveli','Dadra and Nagar Haveli'),
('Daman and Diu','Daman and Diu'),
('Delhi','Delhi'),
('Goa','Goa'),
('Gujarat','Gujarat'),
('Haryana','Haryana'),
('Himachal Pradesh','Himachal Pradesh'),
('Jammu and Kashmir','Jammu and Kashmir'),
('Jharkhand','Jharkhand'),
('Karnataka','Karnataka'),
('Kerala','Kerala'),
('Lakshadweep','Lakshadweep'),
('Madhya Pradesh','Madhya Pradesh'),
('Maharashtra','Maharashtra'),
('Manipur','Manipur'),
('Meghalaya','Meghalaya'),
('Mizoram','Mizoram'),
('Nagaland','Nagaland'),
('Odisha','Odisha'),
('Puducherry','Puducherry'),
('Punjab','Punjab'),
('Rajasthan','Rajasthan'),
('Sikkim','Sikkim'),
('Tamil Nadu','Tamil Nadu'),
('Telangana','Telangana'),
('Tripura','Tripura'),
('Uttar Pradesh','Uttar Pradesh'),
('Uttarakhand','Uttarakhand'),
('West Bengal','West Bengal'),
]

Income_Range = [
('None','None'),
('1k-9k','1k-9k'),
('10k-30k','10k-30k'),
('31k-40k','31k-40k'),
('41k-50k','41k-50k'),
('Above 50k', 'Above 50k'),
]

Education_choice = [
 ('Natural and Physical Sciences','Natural and Physical Sciences'),
 ('Information Technology','Information Technology'),
 ('Engineering and Related Technologies','Engineering and Related Technologies'),
 ('Architecture and Building','Architecture and Building'),
 ('Agriculture, Environmental and Related Studies','Agriculture, Environmental and Related Studies'),
 ('Health','Health'),
 ('Education','Education'),
 ('Management and Commerce','Management and Commerce'),
 ('Society and Culture','Society and Culture'),
 ('Creative Arts','Creative Arts'),
 ('Food, Hospitality and Personal Services','Food, Hospitality and Personal Services'),
 ('Mixed Field Programs','Mixed Field Programs'),
]


class UserCreateModel(User, PermissionsMixin):

    def __str__(self):
        return self.username

    class  Meta():
        db_table = "User_Credential"

class Profile(models.Model):

    user = models.ForeignKey(User_o, on_delete=models.CASCADE)
    image = models.ImageField(default = 'b4.jpg' , upload_to='profile_pics')
    # image_thumbnail = ImageSpecField(source= 'image', processors = [ResizeToFill(150,150)],format='JPEG', options = {'quality':60})

    Age = models.CharField(max_length = 50, choices = Age_range,default = 'Age')
    Gender = models.CharField(max_length = 20, choices = Gender,default='gender')
    Education = models.CharField(max_length = 100 , choices = Education_choice, default= 'Education')
    Profession = models.CharField(max_length=50,choices=Profession_choice)
    State = models.CharField(max_length= 50 ,choices = State_Choice,default='State')
    Income = models.CharField(max_length=20,choices = Income_Range,default='Income')
    Interest= MultiSelectField(choices=Interest_choice)

    def __str__(self):
        return self.user.username

    class  Meta():
        db_table = "Profile"
