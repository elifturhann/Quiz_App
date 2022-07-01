
<img src='/FlightReservationERD.png' ref=''>

# SWAGGER

https://drf-yasg.readthedocs.io/en/stable/readme.html

-Bir projenin API ve dökümantasyon dizayn etmek için kullanılıyor. 
-Proje üzerinde yapılan değişiklikler dökümantasyona yansıyor. 
-Sağlamış olduğuara yüz ile test imkanı sağlıyor.
-

* kurulumu ;

pip install drf-yasg

```html
INSTALLED_APPS = [
    # ...'django.contrib.staticfiles',
    # required for serving swagger ui's css/js files
    # Third party apps:


    'drf_yasg',# 
    
    ...]
```    

```html

```




project urls.py içerisine => 

```html
from django.contrib import admin
from django.urls import path, include
<!-- Three modules for swagger: -->
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi




schema_view = get_schema_view(
    openapi.Info(
        title="Flight Reservation API",
        default_version="v1",
        description="Flight Reservation API project provides flight and reservation info",
        terms_of_service="#",
        contact=openapi.Contact(email="yildirimesutcw@gmail.com"),  # Change e-mail on this line!
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path("admin/", admin.site.urls),

    # Url paths for swagger:
    path("swagger(<format>\.json|\.yaml)", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    <!-- path('__debug__/', include('debug_toolbar.urls')), -->
]

```

python manage.py migrate 

# Debug Toolbar

proje dosyasında history,
settings,
headers
request
SQL
static files
templates
cache
signals
logging

gibi başlıklar ile projede kontrol panelii oluşturuyor,

* kurulumu

```html
pip install django-debug-toolbar



INSTALLED_APPS = [
    # ...'django.contrib.staticfiles',
    # required for serving swagger ui's css/js files
    # Third party apps:


    "debug_toolbar" 
    
    ...]


from django.urls import include


urlpatterns = [# ...    


path('__debug__/', include('debug_toolbar.urls'))

,]  



MIDDLEWARE = [

"debug_toolbar.middleware.DebugToolbarMiddleware",

...]


INTERNAL_IPS = [
    
"127.0.0.1",

]
```
# Seperate Dev and Prod Settings

Inside "settings" folder, 
create;
```html


__init__.py => which is the required file to create a python module. yönlendirme işlemi burada yapılıyor

base.py  =>   which will include common settings. ortak dosyaları burada tututoruz


dev.py which will include developmend specific settings.  local dosyalar burada

prod.py => which will include production specific settings. Product kısmına ait dosyalar burada


Copy all the staff inside settings.py to base.py. And delete settings.py

__init__.py =>

from .base import *

env_name = config('ENV_NAME')


if env_name == 'dev':
    from .dev import *

elif env_name == 'prod':
    from .prod import *


.env =>

ENV_NAME = dev ya da prod oluyor

dev.py=>

from .base import *

THIRD_PARTY_APPS = [

"debug_toolbar",
]

INSTALLED_APPS += THIRD_PARTY_APPS



THIRD_PARTY_MIDDLEWARE = [

 "debug_toolbar.middleware.DebugToolbarMiddleware",
]

MIDDLEWARE += THIRD_PARTY_MIDDLEWARE


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

prod.py =>

postgres i tanımladık

from .base import *


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": config("SQL_DATABASE"),
        "USER": config("SQL_USER"),
        "PASSWORD": config("SQL_PASSWORD"),
        "HOST": config("SQL_HOST"),
        "PORT": config("SQL_PORT"),
        "ATOMIC_REQUESTS": True,
    }
}

.env => postgres için env

SQL_DATABASE=flightDB
SQL_USER=postgres
SQL_PASSWORD=postgres
SQL_HOST=localhost
SQL_PORT=5432


```



# Logging
burada gelecek hataların kayır edilmesi için bir file oluşturduk ve bu file da ve terminalde hataları sınıflarına göre listeledik. aşağıdaki kod olduğu gibi bas.py en sonuna ekleniyor
ve otomatik olarak debug.log file oluşuyor.



```html

LOGGING = {
    "version": 1,
    # is set to True then all loggers from the default configuration will be disabled.
    "disable_existing_loggers": True,
    # Formatters describe the exact format of that text of a log record. 
    "formatters": {
        "standard": {
            "format": "[%(levelname)s] %(asctime)s %(name)s: %(message)s"
        },
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    # The handler is the engine that determines what happens to each message in a logger.
    # It describes a particular logging behavior, such as writing a message to the screen, 
    # to a file, or to a network socket.
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "standard",
            "level": "INFO",
            "stream": "ext://sys.stdout",
            },
        'file': {
            'class': 'logging.FileHandler',
            "formatter": "verbose",
            'filename': './debug.log',
            'level': 'WARNING',
        },
    },
    # A logger is the entry point into the logging system.
    "loggers": {
        "django": {
            "handlers": ["console", 'file'],
            # log level describes the severity of the messages that the logger will handle. 
            "level": config("DJANGO_LOG_LEVEL", "INFO"),
            'propagate': True,
            # If False, this means that log messages written to django.request 
            # will not be handled by the django logger.
        },
    },
}


```
.env=>
DJANGO_LOG_LEVEL=INFO



# AUTHENTICATION

projenin auth işlemleri için users app oluşturduk.

users app de auth için ek paket kurulumu ile devam edeceğiz

*** dj-rest-auth ***

https://dj-rest-auth.readthedocs.io/en/latest/index.html

pip install dj-rest-auth

```html


INSTALLED_APPS = (
    ...,
    'rest_framework',
    'rest_framework.authtoken',
    ...,
    'dj_rest_auth'
)

```

python manage.py migrate

app urls.py içinde 

```html
urlpatterns = [
    ...,
    path('dj-rest-auth/', include('dj_rest_auth.urls'))
]

```
patterns ne yönlendirme yapıyoruz.
aşağıda belirtildiği gibi,

ilgili auth işlemlerini seçiyoruz,


```html

users/ auth/ password/reset/ [name='rest_password_reset']
users/ auth/ password/reset/confirm/ [name='rest_password_reset_confirm']
users/ auth/ login/ [name='rest_login']
users/ auth/ logout/ [name='rest_logout']
users/ auth/ user/ [name='rest_user_details']
users/ auth/ password/change/ [name='rest_password_change']

```

bu peketin register işlemleri içinde özelliği bulunmaktada fakat özelleştirilebilirlik açısından biz kendi registerimizi yazdık 

```html


urlpatterns = [
    ...,
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls'))
]
```

ayrıca social hesapları ile auth işlemlerine imkan sağlamaktadır. 



*** register.py ***

** register işlemini ilgili app de seerializers.py da tanımlıyoruz.

User modelinden register işlemini tanımlıyoruz. Burada değiştirmek istediğimiz fields tekrar yazıyoruz.

emaili uniq ve zorunlu olması için tekrar tanımladık,

serializers.py

```html

from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validated_password


class RegisterSerializer(serializers.ModelSerializer):
    email= serializers.EmailField(
        required=True,
 
        # burada dökümantasyondan gelen validatör işlemini kullanıyoruz. User dan mail vardı fakat burada biz required ve uniq olması içinvalidatör işlemi yaptık
        validators=[validators.UniqueValidator(queryset=User.objects.all())]
     ) 
    password = serializers.CharField(
        write_only=True,
        required =True,
        #pass özel hazır validator kullandık
        validators=[validated_password]
        style={"input-type":"password"}
     )
    password2 = serializers.CharField(
        write_only=True,
        required =True,
        #pass özel hazır validator kullandık
        validators=[validated_password]
        style={"input-type":"password"}
     )

     class Meta:
        model=User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "password",
            "password2"
        )
    
    def create(self, validate_data):
        password = validated_data.pop("password")
        validated_data.pop("password2")
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def validate(self, data):
        if data["password"] != data["password2"]
            raise serializers.ValidationError(
                {"password":"password didn't match..."}
            )
        return data 

```

```html


views.py

from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from .serializers import RegisterSerializer


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

```

```html

urls.py 

from django.urls import path, include
from .views import RegisterView


urlpatterns = [
    
    path('auth/', include('dj_rest_auth.urls')),
    path("register/", RegisterView.as_view()),
]

```
```html

base.py

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
       
    ]
}


```

*** signals.py ***
```html


ilgili app de signals.py da 

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=User)
def create_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


create_token satıra sabit gelmekte, üzerinde tanımlanan dekoratır önenli, sender in user modeli create olunca token ni kaydet

apps.py da bu yazılan signalin çalışması için 



from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
    
    (bu ifadeyi tanımlıyoruz, bu ifade olmazsa çalışmaz)
    def ready(self):
        import users.signals
    

register olduktan sonra token da oluşması için view içirisine ekledik, class içine, bunun sebebi user kayıt olduktan sonra token oluyor, tekrar login için response göndermiyoruz. 

def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = serializer.data
        if Token.objects.filter(user=user).exists():
            token = Token.objects.get(user=user)
            data["token"] = token.key
        else:
            data["token"] = "No token created for this user.... :))"
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)
```

*** USERS bilgilerinin frontende gönderilmesi ****

```html


from dj_rest_auth.serializers import TokenSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email"
        )

class CustomTokenSerializer(TokenSerializer):
    user = UserSerializer(read_only=True)

    class Meta(TokenSerializer.Meta):
        fields = (
            "key",
            "user"
        ) 



settigns.py

REST_AUTH_SERIALIZERS = {
    'TOKEN_SERIALIZER': 'users.serializers.CustomTokenSerializer',

}
```
# FLIGHTS APP

*** 1 ***
* Projede kullancağımız tablolar için planlamamızı yaptık.

* login olan userlar

---flight
listelenmiş uçakları görecekler

---reservation 
reservations oluşturma
see only the reservation you have created

* admin/staff

---flight
- listelenmiş uçaklara ait reservationlarıda görecekler
- uçuş ekleyebilecekler

---reservation 
reservations oluşturma
reservation create and all flight view


models.py da 

üç adet tablo oluşturuyoruz.

flight, passenger , reservation ve django modelden aldığımız User 

3 atblodan faydalanarak oluşturduğumuz reservation tablomuzu inceleyelim

```html


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    passenger = models.ManyToManyField(Passenger, related_name='reservations')
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='reservations') 
```

Reservasyonu yapan bir kişi olur. O reservasyon birden fazla kişiye ait olmaz. Yolcu olarak düşünmeyin user kısmını. Reservasyonu yapan kişi yani uygulamaya login olan bir kişi var.

o reservasyonun iiçinde çok sayıda yolcuya bilet almış olabilir.

ama o reservasyonun bir create edeni olacak

o create eden başka reservasyonlar da oluşturabilir bu yüzden many to one bir ilişki var

user - reservasyon tabloları arasında

ama passenger - reservasyon tabloları konusu daha farklı

tabi bu bizim kurduğumuz yapı. Bu kesin bu şekilde olacak değil. Farklı şekilde de düşünüp kurabilirdik.

passenger - reservasyon tablosu arasında manytomany  çünkü bir reservasyonda birden çok kişi olabilir. Örneğin anne-baba-çocuk bir reservasyonda passenger olabilir. Aynı şekilde bu passengerlar birden fazla reservanyonda da olabilirler. Yani many to many oluyor

user : ManyToOne ilişki mevcut, bir kullanacıbir çok reservation yapabilir
user silindiğinde reservationlarıda silincek, User tablasundan aldık

passenger: ManyToMany ilişki mevcut, bir yolcu birden çok reservation içinde bulunabilir, bu reservationun içinde birden fazla yolcu olabilir.yolcu silindiğinde reservation içinde diğer yolcular olduğundan on_delete methodu kullanmadık.

flight : ManyToOne ilişkisi mevcut, bir uçağa birden fazla reservation yapılabilir. uçak slindiğinde reservationlarda iptal olacağından on_delete de Cascade kullandık.


flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='reservations') 


- related_name='reservations' yazamızın sebebi, modeli serializers da dosya içinde çağırdığımızda kullamak için

- örn : reservasyon_tablosu.user_tablosu.user_name

- reverasyon tablosundan user tablosuna oradan da user name ulaştık.

- flight.reservations.all ile o uçuşa ait tüm reservationlar görüntülenebilmektedir.

- child tablosundan parent tablosuna uaşık

-- tabloları oluşturduktan sonra make-mige yaparak db oluşturduk

-- Admin panelde gözükmesi için admin.py içerisne model tablaloalarını kaydettik

-- Oluşturulan abloları listeleyebilmek görüntüleyebilmek ve API oluşturabilemek için serializers.py file oluşturduk

-- modeldeki tabloyu modelserializers ile çağırdık

-- serializersdeki veriyi görüntüleyebilmek için views.py ve urls.py file larına ihtiyacımız var.

-- views.py da views de class ve func yapıları ile gelen veriyi kullanabiliyoruz. bu projede class viewseti kullandık,

-- viewset kullanıldığından urls.py da router yapısı kullanıyoruz. tek bir url pattern ile crud işlemleri yapmamızı sağlıyor

-- bu aşamada api görüntüledik ve post get put delete yapabiliyoruz, herhangi bir kullanıcı kısıtlaması olmadan bu işlemleri yaptık, 2. aşamda kullanıcı permissionsları getirerek ilerleyeceğiz.

---------***2***--------------

oluşturmuş olduğumuztabloları tümkullancılar kullanıcı olmayanlar herkes görebiliyor ve crud işlemleri yapabiliyor, PERMISSIONS tanımlıyoruz.

permissions.py file oluşturduk.

içerisine 
```html


class IsStafforReadOnly(permissions.IsAdminUser):
     
      def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)
```
IsAdminUser ı inheritettik ve sourcode dan yukarıdaki ifadeyi aldık,  sourecoda sadece admin user için şartkoyulmuş biz ek olarak,

SAFE_METHODS: get, options, safe olmayanlar put post delete

request istek varsa get olarak cevap ver

method post, put delete ise admin özelliği ara şeklinde algoritma yazdık

ilgili permissions u kısıtlamam getireceğimiz tablo için views.py class içine yazıyoruz.

from .permission import IsStafforReadOnly

```html

class FlightView(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class =  FlightSerializer
    permission_classes = (IsStafforReadOnly,) 


```
bu yetkilendirmeyi postmanda kontrol edebiliyoruz. staff ve n-login user tokenları ile test edilir  


------- ***3***----------
reservation (relatioship) tablosundan oluşturduğumuz reservasyonlar bu şekilde geliyor, bunları id ile değilde isimleri ile çağıracağız,


```html


[
    {
        "id": 1,
        "user": 1,
        "flight": 2,
        "passenger": [
            1,
            2
        ]
    }
]
```

* Nested olarak tanımlayacağız...


ilgili serializers içinde diğer serializersları çağırdık,


```html


class ReservationSerializer(serializers.ModelSerializer):

    passenger = PassengerSerializer(many=True, required=False)
    # flight = FlightSerializer()
    flight = serializers.StringRelatedField()
    user = serializers.StringRelatedField()
    flight_id = serializers.IntegerField(write_only=True)
    user_id = serializers.IntegerField(write_only=True, required=False)


    class Meta:
        model = Reservation
        # fields = '__all__'
        fields =(
           "id",
           "flight",
           "flight_id",
           "user",
           "user_id",
           "passenger"
        )

```
- field ları çağırken string ve serailizr olarak farklı yöntem kullanabiliriz.Strinfield modeldeki str de tanımlananları getirir.
- StringRelatedField ler post işlemlerinde çalışmıyor, sadece read_only de çalışıyor

- bu sebepler çağırdığımız fileldları id ile de çağırdık, ve write_only olarak tanımladık, sadece created yapılırken kullanılsın diye, 


----- *** 4 *** -----

***Nesned Create***

- Şu an hali hazırda nested olarak gelen tabloda create işlemi yapamadık postmanda, swagger ile örnek gönderilecek post şemasını aldık, postmandan post işlemi başarız oldu

- http://127.0.0.1:8000/flight/resv/ sayfasından da passenger kayıt edemiyoruz. 

- get olayında sorun olmuyor post yaparken sorun olduğu için 

- nested yapı olarak ayarladığımız reservasyon tablosunda create işlemi yapabilmek için serializers da create func tanımlamamız gerekiyor.

- ManyToMany tabloda create işlemi yapacağız. 

- Tek bir işlemle passenger ları create edip reservasyon yapacağız.

```html


def create(self, validated_data):
        passenger_data = validated_data.pop('passenger')
        <!-- datanın içinde pop ile passenger i yakaladık -->
        print(validated_data)
        validated_data['user_id'] = self.context['request'].user.id
        <!-- login olan user atama yaptık, serializers içinde request.user ile atama yapamıyoruz -->
        reservation = Reservation.objects.create(**validated_data)
        <!-- bir reservation da bir çok yolcu olacağından for ile devam ettik -->
        for passenger in passenger_data:
            pas = Passenger.objects.create(**passenger)
            reservation.passenger.add(pas)
        reservation.save()
        return reservation

```

----***5***-------


* oluşturulan reservasyonları kullanıcılara göre kısıtlama

- views.py da yazdığımız bu kod ile tüm reservasyonları çağırdık,

- class ReservationView(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class =  ReservationSerializer


- bu kodu override edeceğiz, ModelViewSet -> GenericAPIViews den

 def get_queryset(self):
        return super().get_queryset()

yukarıdaki kodu aldık ve aşağıdaki gibi override edeceğiz.

```html


 def get_queryset(self):
       queryset = super().get_queryset()
    #    queryset = Reservation.objects.all() yukarıdaki ile aynı 
       if self.request.user.is_staff:
           return queryset
       return queryset.filter(user=self.request.user)          


```
tüm veriyi aldık, eğer is_staff ise hepsini göster,
değilse user olan ile queryseti oluşturan user eşit olanları göster

---***6***----

- Staff users flight/flights listesi geldiğinde nu uçuşlara ait reservationlarıda görmesini sağlayacağız.

serializers.py =>

```html


class StaffFlightSerializer(serializers.ModelSerializer):
    
    reservations = ReservationSerializer(many=True, read_only=True)
    
    class Meta:
        model = Flight
        fields = (
            "id",
            "flight_number",
            "operation_airlines",
            "departure_city",
            "arrival_city",
            "date_of_departure",
            "etd",
            "reservations",
        )
```
- tanımladığımız serializers class da, Reservation modelinde tanımladığımız related_name='reservations' kullanıyoruz. get methodunda kullanılması için read_only=True yazdık, 

- oluşturduğumuz serializer view içinde kullanacağız, fakat FlightView için tanımladığımız serializer vardı, bu view içinde override işlemi yapıyoruz.

- ModelViewSet-> GenericAPIView -> def get_serializer_class(self): 

kullandık, burada gelen isteğe göre serializer kullanılabiliyor.

```html

def get_serializer_class(self):
        serializer = super().get_serializer_class()
        if self.request.user.is_staff:
            return StaffFlightSerializer
        return serializer 


```

---- ***7*** ----

-Eski uçuşların gözükmemesi

from datetime import datetime, date

python date ve datetime modüllerini import ettik

strftime('%H:%M:%S') pythondan gelen bir özellik

```html


 def get_queryset(self):
        now = datetime.now()
        current_time = now.strftime('%H:%M:%S')
        today = date.today()

        if self.request.user.is_staff:
            return super().get_queryset()
            <!-- staff ise hepsini görsün -->
        else:
            queryset = Flight.objects.filter(date_of_departure__gt=today)
            <!-- bugünden büyük olanları aldık -->
            if Flight.objects.filter(date_of_departure=today):
                today_qs =Flight.objects.filter(date_of_departure=today).filter(etd__gt=current_time)
                <!-- tarih bugün ve saat kısıtlaması yaptık -->
                queryset = queryset.union(today_qs)
                <!-- yukarıdaki iki sorguyu birleştirdik. -->
            return queryset  


```




















