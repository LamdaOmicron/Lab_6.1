from rest_framework import serializers
from .models import Character

class CharacterSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения характеристик персонажа"""
    type_display = serializers.CharField(source='get_type_display', read_only=True)
    class_name_display = serializers.CharField(source='get_class_name_display', read_only=True)
    ancestry_display = serializers.CharField(source='get_ancestry_display', read_only=True)
    heritage_display = serializers.CharField(source='get_heritage_display', read_only=True)
    background_display = serializers.CharField(source='get_background_display', read_only=True)
    is_alive = serializers.ReadOnlyField()

    class Meta:
        model = Character
        fields = [
            'id', 'name', 'type', 'type_display', 'level', 'class_name', 'class_name_display',
            'ancestry', 'ancestry_display', 'heritage', 'heritage_display', 
            'background', 'background_display', 'hp_max', 'hp_current', 'speed',
            'is_alive', 'owner', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'is_alive', 'created_at', 'updated_at']


class CharacterCreateRequestSerializer(serializers.Serializer):
    """Сериализатор для создания нового персонажа"""
    name = serializers.CharField(help_text="Имя персонажа", max_length=255)
    type = serializers.ChoiceField(
        choices=[('player', 'Player Character'), ('npc', 'Non-Player Character'), ('monster', 'Monster')],
        default='player',
        help_text="Тип персонажа"
    )
    level = serializers.IntegerField(default=1, min_value=1, max_value=20, help_text="Уровень персонажа")
    class_name = serializers.ChoiceField(
        choices=[
            ('fighter', 'Fighter'), ('wizard', 'Wizard'), ('rogue', 'Rogue'),
            ('cleric', 'Cleric'), ('ranger', 'Ranger'), ('barbarian', 'Barbarian'),
            ('bard', 'Bard'), ('druid', 'Druid'), ('monk', 'Monk'),
            ('paladin', 'Paladin'), ('sorcerer', 'Sorcerer'), ('warlock', 'Warlock'),
        ],
        default='fighter',
        help_text="Класс персонажа"
    )
    ancestry = serializers.ChoiceField(
        choices=[
            ('human', 'Human'), ('elf', 'Elf'), ('dwarf', 'Dwarf'),
            ('halfling', 'Halfling'), ('orc', 'Orc'), ('gnome', 'Gnome'),
        ],
        default='human',
        help_text="Происхождение"
    )
    heritage = serializers.ChoiceField(
        choices=[
            ('none', 'None'), ('ancient', 'Ancient Bloodline'),
            ('celestial', 'Celestial Touch'), ('fiendish', 'Fiendish Heritage'),
            ('shadow', 'Shadow Touched'),
        ],
        default='none',
        help_text="Наследие"
    )
    background = serializers.ChoiceField(
        choices=[
            ('acolyte', 'Acolyte'), ('criminal', 'Criminal'), ('folk_hero', 'Folk Hero'),
            ('noble', 'Noble'), ('sage', 'Sage'), ('soldier', 'Soldier'), ('urchin', 'Urchin'),
        ],
        default='folk_hero',
        help_text="Предыстория"
    )
    hp_max = serializers.IntegerField(default=10, min_value=1, help_text="Максимальное здоровье")
    hp_current = serializers.IntegerField(default=10, min_value=0, help_text="Текущее здоровье")
    speed = serializers.IntegerField(default=30, min_value=0, help_text="Скорость перемещения (футы)")


class CharacterUpdateRequestSerializer(serializers.Serializer):
    """Сериализатор для полного обновления персонажа"""
    name = serializers.CharField(help_text="Имя персонажа", max_length=255)
    type = serializers.ChoiceField(
        choices=[('player', 'Player Character'), ('npc', 'Non-Player Character'), ('monster', 'Monster')],
        help_text="Тип персонажа"
    )
    level = serializers.IntegerField(min_value=1, max_value=20, help_text="Уровень персонажа")
    class_name = serializers.ChoiceField(
        choices=[
            ('fighter', 'Fighter'), ('wizard', 'Wizard'), ('rogue', 'Rogue'),
            ('cleric', 'Cleric'), ('ranger', 'Ranger'), ('barbarian', 'Barbarian'),
            ('bard', 'Bard'), ('druid', 'Druid'), ('monk', 'Monk'),
            ('paladin', 'Paladin'), ('sorcerer', 'Sorcerer'), ('warlock', 'Warlock'),
        ],
        help_text="Класс персонажа"
    )
    ancestry = serializers.ChoiceField(
        choices=[
            ('human', 'Human'), ('elf', 'Elf'), ('dwarf', 'Dwarf'),
            ('halfling', 'Halfling'), ('orc', 'Orc'), ('gnome', 'Gnome'),
        ],
        help_text="Происхождение"
    )
    heritage = serializers.ChoiceField(
        choices=[
            ('none', 'None'), ('ancient', 'Ancient Bloodline'),
            ('celestial', 'Celestial Touch'), ('fiendish', 'Fiendish Heritage'),
            ('shadow', 'Shadow Touched'),
        ],
        help_text="Наследие"
    )
    background = serializers.ChoiceField(
        choices=[
            ('acolyte', 'Acolyte'), ('criminal', 'Criminal'), ('folk_hero', 'Folk Hero'),
            ('noble', 'Noble'), ('sage', 'Sage'), ('soldier', 'Soldier'), ('urchin', 'Urchin'),
        ],
        help_text="Предыстория"
    )
    hp_max = serializers.IntegerField(min_value=1, help_text="Максимальное здоровье")
    hp_current = serializers.IntegerField(min_value=0, help_text="Текущее здоровье")
    speed = serializers.IntegerField(min_value=0, help_text="Скорость перемещения (футы)")


class CharacterPatchRequestSerializer(serializers.Serializer):
    """Сериализатор для частичного обновления персонажа"""
    name = serializers.CharField(help_text="Имя персонажа", max_length=255, required=False)
    type = serializers.ChoiceField(
        choices=[('player', 'Player Character'), ('npc', 'Non-Player Character'), ('monster', 'Monster')],
        required=False,
        help_text="Тип персонажа"
    )
    level = serializers.IntegerField(min_value=1, max_value=20, required=False, help_text="Уровень персонажа")
    class_name = serializers.ChoiceField(
        choices=[
            ('fighter', 'Fighter'), ('wizard', 'Wizard'), ('rogue', 'Rogue'),
            ('cleric', 'Cleric'), ('ranger', 'Ranger'), ('barbarian', 'Barbarian'),
            ('bard', 'Bard'), ('druid', 'Druid'), ('monk', 'Monk'),
            ('paladin', 'Paladin'), ('sorcerer', 'Sorcerer'), ('warlock', 'Warlock'),
        ],
        required=False,
        help_text="Класс персонажа"
    )
    ancestry = serializers.ChoiceField(
        choices=[
            ('human', 'Human'), ('elf', 'Elf'), ('dwarf', 'Dwarf'),
            ('halfling', 'Halfling'), ('orc', 'Orc'), ('gnome', 'Gnome'),
        ],
        required=False,
        help_text="Происхождение"
    )
    heritage = serializers.ChoiceField(
        choices=[
            ('none', 'None'), ('ancient', 'Ancient Bloodline'),
            ('celestial', 'Celestial Touch'), ('fiendish', 'Fiendish Heritage'),
            ('shadow', 'Shadow Touched'),
        ],
        required=False,
        help_text="Наследие"
    )
    background = serializers.ChoiceField(
        choices=[
            ('acolyte', 'Acolyte'), ('criminal', 'Criminal'), ('folk_hero', 'Folk Hero'),
            ('noble', 'Noble'), ('sage', 'Sage'), ('soldier', 'Soldier'), ('urchin', 'Urchin'),
        ],
        required=False,
        help_text="Предыстория"
    )
    hp_max = serializers.IntegerField(min_value=1, required=False, help_text="Максимальное здоровье")
    hp_current = serializers.IntegerField(min_value=0, required=False, help_text="Текущее здоровье")
    speed = serializers.IntegerField(min_value=0, required=False, help_text="Скорость перемещения (футы)")


class PaginationMetaSerializer(serializers.Serializer):
    """Сериализатор для метаданных пагинации"""
    total = serializers.IntegerField()
    page = serializers.IntegerField()
    limit = serializers.IntegerField()
    totalPages = serializers.IntegerField()


class CharacterListResponseSerializer(serializers.Serializer):
    """Сериализатор для списка персонажей с пагинацией"""
    data = CharacterSerializer(many=True)
    meta = PaginationMetaSerializer()


class ErrorResponseSerializer(serializers.Serializer):
    """Сериализатор для ошибок"""
    error = serializers.CharField(default="unauthorized")