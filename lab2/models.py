from django.db import models
import uuid
from users.models import User

class Work(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # Уникальный идентификатор произведения
    title = models.CharField(max_length=255)  # Название работы
    description = models.TextField()  # Описание или аннотация
    author_name = models.CharField(max_length=255)  # Имя автора
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='works', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания
    updated_at = models.DateTimeField(auto_now=True)  # Дата последнего обновления
    deleted_at = models.DateTimeField(null=True, blank=True)  # Дата мягкого удаления

    def __str__(self):
        return self.title


class Character(models.Model):
    """Модель персонажа для RPG-системы"""
    CHARACTER_TYPES = [
        ('player', 'Player Character'),
        ('npc', 'Non-Player Character'),
        ('monster', 'Monster'),
    ]
    
    ANCESTRIES = [
        ('human', 'Human'),
        ('elf', 'Elf'),
        ('dwarf', 'Dwarf'),
        ('halfling', 'Halfling'),
        ('orc', 'Orc'),
        ('gnome', 'Gnome'),
    ]
    
    CLASSES = [
        ('fighter', 'Fighter'),
        ('wizard', 'Wizard'),
        ('rogue', 'Rogue'),
        ('cleric', 'Cleric'),
        ('ranger', 'Ranger'),
        ('barbarian', 'Barbarian'),
        ('bard', 'Bard'),
        ('druid', 'Druid'),
        ('monk', 'Monk'),
        ('paladin', 'Paladin'),
        ('sorcerer', 'Sorcerer'),
        ('warlock', 'Warlock'),
    ]
    
    HERITAGES = [
        ('none', 'None'),
        ('ancient', 'Ancient Bloodline'),
        ('celestial', 'Celestial Touch'),
        ('fiendish', 'Fiendish Heritage'),
        ('shadow', 'Shadow Touched'),
    ]
    
    BACKGROUNDS = [
        ('acolyte', 'Acolyte'),
        ('criminal', 'Criminal'),
        ('folk_hero', 'Folk Hero'),
        ('noble', 'Noble'),
        ('sage', 'Sage'),
        ('soldier', 'Soldier'),
        ('urchin', 'Urchin'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, help_text="Имя персонажа")
    type = models.CharField(max_length=20, choices=CHARACTER_TYPES, default='player', help_text="Тип персонажа")
    level = models.PositiveIntegerField(default=1, help_text="Уровень персонажа")
    class_name = models.CharField(max_length=50, choices=CLASSES, default='fighter', help_text="Класс персонажа")
    ancestry = models.CharField(max_length=50, choices=ANCESTRIES, default='human', help_text="Происхождение")
    heritage = models.CharField(max_length=50, choices=HERITAGES, default='none', help_text="Наследие")
    background = models.CharField(max_length=50, choices=BACKGROUNDS, default='folk_hero', help_text="Предыстория")
    hp_max = models.PositiveIntegerField(default=10, help_text="Максимальное здоровье")
    hp_current = models.PositiveIntegerField(default=10, help_text="Текущее здоровье")
    speed = models.PositiveIntegerField(default=30, help_text="Скорость перемещения (футы)")
    
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='characters', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} (Lvl {self.level} {self.class_name})"
    
    @property
    def is_alive(self):
        return self.hp_current > 0