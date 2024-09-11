from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

# parsing the allowed identifiers from settings
SchemeChoices = []
for choices in settings.GEOLUMINATE_ALLOWED_IDENTIFIERS.values():
    for val in choices.items():
        rev_val = tuple(reversed(val))
        if rev_val not in SchemeChoices:
            SchemeChoices.append(rev_val)


class Visibility(models.IntegerChoices):
    PRIVATE = 0, _("Private")
    PUBLIC = 1, _("Public")


HAS_TAGS = [
    ("has_funding", _("Has Funding")),
    ("has_equipment", _("Has Instruments")),
]

NEEDS_TAGS = [
    ("needs_collaborators", _("Collaborators")),
    ("funding_wanted", _("Needs Funding")),
    ("equipment_wanted", _("Needs Instruments")),
]

DiscoveryTags = HAS_TAGS + NEEDS_TAGS


iso_639_1_languages = [
    (
        "Common",
        [
            ("en", _("English")),
            ("es", _("Spanish")),
            ("fr", _("French")),
            ("de", _("German")),
            ("it", _("Italian")),
            ("pt", _("Portuguese")),
            ("ru", _("Russian")),
            ("zh", _("Chinese")),
            ("ja", _("Japanese")),
            ("ar", _("Arabic")),
        ],
    ),
    (
        "Other",
        [
            ("aa", _("Afar")),
            ("ab", _("Abkhazian")),
            ("ae", _("Avestan")),
            ("af", _("Afrikaans")),
            ("ak", _("Akan")),
            ("am", _("Amharic")),
            ("an", _("Aragonese")),
            # ("ar", _("Arabic")),
            ("as", _("Assamese")),
            ("av", _("Avaric")),
            ("ay", _("Aymara")),
            ("az", _("Azerbaijani")),
            ("ba", _("Bashkir")),
            ("be", _("Belarusian")),
            ("bg", _("Bulgarian")),
            ("bh", _("Bihari")),
            ("bi", _("Bislama")),
            ("bm", _("Bambara")),
            ("bn", _("Bengali")),
            ("bo", _("Tibetan")),
            ("br", _("Breton")),
            ("bs", _("Bosnian")),
            ("ca", _("Catalan")),
            ("ce", _("Chechen")),
            ("ch", _("Chamorro")),
            ("co", _("Corsican")),
            ("cr", _("Cree")),
            ("cs", _("Czech")),
            ("cu", _("Church Slavic")),
            ("cv", _("Chuvash")),
            ("cy", _("Welsh")),
            ("da", _("Danish")),
            # ("de", _("German")),
            ("dv", _("Divehi")),
            ("dz", _("Dzongkha")),
            ("ee", _("Ewe")),
            ("el", _("Greek")),
            # ("en", _("English")),
            ("eo", _("Esperanto")),
            # ("es", _("Spanish")),
            ("et", _("Estonian")),
            ("eu", _("Basque")),
            ("fa", _("Persian")),
            ("ff", _("Fulah")),
            ("fi", _("Finnish")),
            ("fj", _("Fijian")),
            ("fo", _("Faroese")),
            # ("fr", _("French")),
            ("fy", _("Western Frisian")),
            ("ga", _("Irish")),
            ("gd", _("Scottish Gaelic")),
            ("gl", _("Galician")),
            ("gn", _("Guarani")),
            ("gu", _("Gujarati")),
            ("gv", _("Manx")),
            ("ha", _("Hausa")),
            ("he", _("Hebrew")),
            ("hi", _("Hindi")),
            ("ho", _("Hiri Motu")),
            ("hr", _("Croatian")),
            ("ht", _("Haitian")),
            ("hu", _("Hungarian")),
            ("hy", _("Armenian")),
            ("hz", _("Herero")),
            ("ia", _("Interlingua")),
            ("id", _("Indonesian")),
            ("ie", _("Interlingue")),
            ("ig", _("Igbo")),
            ("ii", _("Sichuan Yi")),
            ("ik", _("Inupiaq")),
            ("io", _("Ido")),
            ("is", _("Icelandic")),
            # ("it", _("Italian")),
            ("iu", _("Inuktitut")),
            # ("ja", _("Japanese")),
            ("jv", _("Javanese")),
            ("ka", _("Georgian")),
            ("kg", _("Kongo")),
            ("ki", _("Kikuyu")),
            ("kj", _("Kwanyama")),
            ("kk", _("Kazakh")),
            ("kl", _("Kalaallisut")),
            ("km", _("Central Khmer")),
            ("kn", _("Kannada")),
            ("ko", _("Korean")),
            ("kr", _("Kanuri")),
            ("ks", _("Kashmiri")),
            ("ku", _("Kurdish")),
            ("kv", _("Komi")),
            ("kw", _("Cornish")),
            ("ky", _("Kirghiz")),
            ("la", _("Latin")),
            ("lb", _("Luxembourgish")),
            ("lg", _("Ganda")),
            ("li", _("Limburgan")),
            ("ln", _("Lingala")),
            ("lo", _("Lao")),
            ("lt", _("Lithuanian")),
            ("lu", _("Luba-Katanga")),
            ("lv", _("Latvian")),
            ("mg", _("Malagasy")),
            ("mh", _("Marshallese")),
            ("mi", _("Maori")),
            ("mk", _("Macedonian")),
            ("ml", _("Malayalam")),
            ("mn", _("Mongolian")),
            ("mr", _("Marathi")),
            ("ms", _("Malay")),
            ("mt", _("Maltese")),
            ("my", _("Burmese")),
            ("na", _("Nauru")),
            ("nb", _("Norwegian Bokmål")),
            ("nd", _("North Ndebele")),
            ("ne", _("Nepali")),
            ("ng", _("Ndonga")),
            ("nl", _("Dutch")),
            ("nn", _("Norwegian Nynorsk")),
            ("no", _("Norwegian")),
            ("nr", _("South Ndebele")),
            ("nv", _("Navajo")),
            ("ny", _("Chichewa")),
            ("oc", _("Occitan")),
            ("oj", _("Ojibwa")),
            ("om", _("Oromo")),
            ("or", _("Oriya")),
            ("os", _("Ossetian")),
            ("pa", _("Panjabi")),
            ("pi", _("Pali")),
            ("pl", _("Polish")),
            ("ps", _("Pashto")),
            # ("pt", _("Portuguese")),
            ("qu", _("Quechua")),
            ("rm", _("Romansh")),
            ("rn", _("Rundi")),
            ("ro", _("Romanian")),
            # ("ru", _("Russian")),
            ("rw", _("Kinyarwanda")),
            ("sa", _("Sanskrit")),
            ("sc", _("Sardinian")),
            ("sd", _("Sindhi")),
            ("se", _("Northern Sami")),
            ("sg", _("Sango")),
            ("si", _("Sinhala")),
            ("sk", _("Slovak")),
            ("sl", _("Slovenian")),
            ("sm", _("Samoan")),
            ("sn", _("Shona")),
            ("so", _("Somali")),
            ("sq", _("Albanian")),
            ("sr", _("Serbian")),
            ("ss", _("Swati")),
            ("st", _("Southern So")),
            ("su", _("Sundanese")),
            ("sv", _("Swedish")),
            ("sw", _("Swahili")),
            ("ta", _("Tamil")),
            ("te", _("Telugu")),
            ("tg", _("Tajik")),
            ("th", _("Thai")),
            ("ti", _("Tigrinya")),
            ("tk", _("Turkmen")),
            ("tl", _("Tagalog")),
            ("tn", _("Tswana")),
            ("to", _("Tonga")),
            ("tr", _("Turkish")),
            ("ts", _("Tsonga")),
            ("tt", _("Tatar")),
            ("tw", _("Twi")),
            ("ty", _("Tahitian")),
            ("ug", _("Uighur")),
            ("uk", _("Ukrainian")),
            ("ur", _("Urdu")),
            ("uz", _("Uzbek")),
            ("ve", _("Venda")),
            ("vi", _("Vietnamese")),
            ("vo", _("Volapük")),
            ("wa", _("Walloon")),
            ("wo", _("Wolof")),
            ("xh", _("Xhosa")),
            ("yi", _("Yiddish")),
            ("yo", _("Yoruba")),
            ("za", _("Zhuang")),
            # ("zh", _("Chinese")),
            ("zu", _("Zulu")),
        ],
    ),
]