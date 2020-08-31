from rest_framework import serializers

from .models import Pet

class PetSerializer(serializers.ModelSerializer):
    owner_name              = serializers.SerializerMethodField(read_only=True)
    # image               = serializers.SerializerMethodField(read_only=True)
    name                = serializers.SerializerMethodField(read_only=True)
    pet_type            = serializers.SerializerMethodField(read_only=True)
    breed               = serializers.SerializerMethodField(read_only=True)
    gender              = serializers.SerializerMethodField(read_only=True)
    son                 = serializers.SerializerMethodField(read_only=True)
    weight              = serializers.SerializerMethodField(read_only=True)
    coat                = serializers.SerializerMethodField(read_only=True)
    birthday            = serializers.SerializerMethodField(read_only=True)
    allergies_notes     = serializers.SerializerMethodField(read_only=True)
    notes               = serializers.SerializerMethodField(read_only=True)
    vaccine             = serializers.SerializerMethodField(read_only=True)
    allergies           = serializers.SerializerMethodField(read_only=True)
    anal_gland          = serializers.SerializerMethodField(read_only=True)
    arthirits           = serializers.SerializerMethodField(read_only=True)
    blind               = serializers.SerializerMethodField(read_only=True)
    trachea             = serializers.SerializerMethodField(read_only=True)
    deaf                = serializers.SerializerMethodField(read_only=True)
    diabetic            = serializers.SerializerMethodField(read_only=True)
    standing            = serializers.SerializerMethodField(read_only=True)
    epileptic           = serializers.SerializerMethodField(read_only=True)
    heart               = serializers.SerializerMethodField(read_only=True)
    hip                 = serializers.SerializerMethodField(read_only=True)
    hot                 = serializers.SerializerMethodField(read_only=True)
    incontinence        = serializers.SerializerMethodField(read_only=True)
    kidney              = serializers.SerializerMethodField(read_only=True)
    moles               = serializers.SerializerMethodField(read_only=True)
    pancreatitis        = serializers.SerializerMethodField(read_only=True)
    ear                 = serializers.SerializerMethodField(read_only=True)
    skin                = serializers.SerializerMethodField(read_only=True)
    tooth               = serializers.SerializerMethodField(read_only=True)
    tumors              = serializers.SerializerMethodField(read_only=True)
    anxiety             = serializers.SerializerMethodField(read_only=True)
    cage                = serializers.SerializerMethodField(read_only=True)
    clippers            = serializers.SerializerMethodField(read_only=True)
    dryer               = serializers.SerializerMethodField(read_only=True)
    nail                = serializers.SerializerMethodField(read_only=True)
    water               = serializers.SerializerMethodField(read_only=True)
    shedding            = serializers.SerializerMethodField(read_only=True)
    hernia              = serializers.SerializerMethodField(read_only=True)
    energy              = serializers.SerializerMethodField(read_only=True)
    biting              = serializers.SerializerMethodField(read_only=True)
    leash               = serializers.SerializerMethodField(read_only=True)
    soiler              = serializers.SerializerMethodField(read_only=True)
    prefumes            = serializers.SerializerMethodField(read_only=True)
    photo               = serializers.SerializerMethodField(read_only=True)
    animal              = serializers.SerializerMethodField(read_only=True)
    people              = serializers.SerializerMethodField(read_only=True)
    clipper_burn        = serializers.SerializerMethodField(read_only=True)
    senior              = serializers.SerializerMethodField(read_only=True)
    table               = serializers.SerializerMethodField(read_only=True)
    team                = serializers.SerializerMethodField(read_only=True)
    chew                = serializers.SerializerMethodField(read_only=True)
    timid               = serializers.SerializerMethodField(read_only=True)
    barker              = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Pet
        fields = [
            'owner_name', 'name', 'pet_type', 'breed', 'gender', 'son', 'weight', 'coat','birthday', 'allergies_notes',
            'notes', 'vaccine', 'allergies', 'anal_gland', 'arthirits', 'blind', 'trachea','deaf', 'diabetic', 'standing',
            'epileptic', 'heart', 'hip', 'hot', 'incontinence', 'kidney', 'moles','pancreatitis', 'ear', 'skin', 'tooth', 'tumors',
            'anxiety', 'cage', 'clippers', 'dryer', 'nail', 'water', 'shedding', 'hernia','energy', 'biting', 'leash', 'soiler', 'prefumes',
            'photo', 'animal', 'people', 'clipper_burn', 'senior', 'table', 'team', 'chew','timid', 'barker'
        ]
    

    def get_owner_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
    
    # def get_image(self, obj):
    #     return obj.image

    def get_name(self, obj):
        return obj.name
    
    def get_pet_type(self, obj):
        return obj.pet_type

    def get_breed(self, obj):
        return obj.breed

    def get_gender(self, obj):
        return obj.gender

    def get_son(self, obj):
        return obj.son

    def get_weight(self, obj):
        return obj.weight
    
    def get_coat(self, obj):
        return obj.coat

    def get_birthday(self, obj):
        return obj.birthday

    def get_allergies_notes(self, obj):
        return obj.allergies_notes

    def get_notes(self, obj):
        return obj.notes

    def get_vaccine(self, obj):
        return obj.vaccine

    def get_allergies(self, obj):
        return obj.allergies

    def get_anal_gland(self, obj):
        return obj.anal_gland

    def get_arthirits(self, obj):
        return obj.arthirits

    def get_blind(self, obj):
        return obj.blind

    def get_trachea(self, obj):
        return obj.trachea

    def get_deaf(self, obj):
        return obj.deaf

    def get_diabetic(self, obj):
        return obj.diabetic

    def get_standing(self, obj):
        return obj.standing

    def get_epileptic(self, obj):
        return obj.epileptic

    def get_heart(self, obj):
        return obj.heart

    def get_hip(self, obj):
        return obj.hip

    def get_hot(self, obj):
        return obj.hot

    def get_incontinence(self, obj):
        return obj.incontinence

    def get_kidney(self, obj):
        return obj.kidney

    def get_moles(self, obj):
        return obj.moles

    def get_pancreatitis(self, obj):
        return obj.pancreatitis

    def get_ear(self, obj):
        return obj.ear

    def get_skin(self, obj):
        return obj.skin

    def get_tooth(self, obj):
        return obj.tooth

    def get_tumors(self, obj):
        return obj.tumors

    def get_anxiety(self, obj):
        return obj.anxiety

    def get_cage(self, obj):
        return obj.cage

    def get_clippers(self, obj):
        return obj.clippers

    def get_dryer(self, obj):
        return obj.dryer

    def get_nail(self, obj):
        return obj.nail

    def get_water(self, obj):
        return obj.water

    def get_shedding(self, obj):
        return obj.shedding

    def get_hernia(self, obj):
        return obj.hernia

    def get_energy(self, obj):
        return obj.energy

    def get_biting(self, obj):
        return obj.biting

    def get_leash(self, obj):
        return obj.leash

    def get_soiler(self, obj):
        return obj.soiler

    def get_prefumes(self, obj):
        return obj.prefumes

    def get_photo(self, obj):
        return obj.photo

    def get_animal(self, obj):
        return obj.animal

    def get_people(self, obj):
        return obj.people

    def get_clipper_burn(self, obj):
        return obj.clipper_burn

    def get_senior(self, obj):
        return obj.senior

    def get_table(self, obj):
        return obj.table

    def get_team(self, obj):
        return obj.team

    def get_chew(self, obj):
        return obj.chew

    def get_timid(self, obj):
        return obj.timid

    def get_barker(self, obj):
        return obj.barker

class PetCreateSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = Pet
        fields = [
            'owner_name', 'name', 'pet_type', 'breed', 'gender', 'son', 'weight', 'coat','birthday', 'allergies_notes',
            'notes', 'vaccine', 'allergies', 'anal_gland', 'arthirits', 'blind', 'trachea','deaf', 'diabetic', 'standing',
            'epileptic', 'heart', 'hip', 'hot', 'incontinence', 'kidney', 'moles','pancreatitis', 'ear', 'skin', 'tooth', 'tumors',
            'anxiety', 'cage', 'clippers', 'dryer', 'nail', 'water', 'shedding', 'hernia','energy', 'biting', 'leash', 'soiler', 'prefumes',
            'photo', 'animal', 'people', 'clipper_burn', 'senior', 'table', 'team', 'chew','timid', 'barker'
        ]


class PetListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pet
        fields = [
            'id','name','pet_type','breed','gender'
        ]