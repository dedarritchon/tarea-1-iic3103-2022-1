from .city import City

from .airports import (
    ronald_reagan,
    washington_dulles,
    baltimore_washington,
    melbourne_international,
    essendon,
    avalon,
    pekin_international,
    peking_daxing,
    zhege_jichang,
    fez_saiss,
    mohammed,
    muzayaf,
    arturo_merino_benitez,
    charles_de_gaulle,
    orly,
    beauvais_tille
)

from .hotels import (
    grand_hyatt_washington,
    hilton_garden,
    embassy_row,
    lancemore_crossley,
    grand_hyatt_melbourne,
    crown_metropol,
    grand_skylight,
    beijing_jinjiang,
    sunworld_dynasty,
    palais_medina,
    zalagh_parc_palace,
    dar_tahri,
    plaza_san_francisco,
    singular,
    ritz_carlton,
    balzac,
    intercontinental_le_grand,
    renaissance_paris
)

from .turisms import (
    pentagon,
    white_house,
    smithsonians,
    melbourne_zoo,
    icebar,
    great_ocean_road,
    great_wall,
    forbidden_city,
    tiananmen,
    blue_city,
    desert_tour,
    la_medina_tour,
    sky_costanera,
    santa_rita_winery,
    big_bus_tour,
    eiffel_tower,
    louvre,
    notre_dame
)

santiago = City('Santiago', sku='C1')

santiago.add_airport(arturo_merino_benitez)

santiago.add_hotel(plaza_san_francisco)
santiago.add_hotel(singular)
#santiago.add_hotel(ritz_carlton)

santiago.add_turism(sky_costanera)
santiago.add_turism(santa_rita_winery)
#santiago.add_turism(big_bus_tour)

melbourne = City('Melbourne', sku='C2')

melbourne.add_airport(melbourne_international)
melbourne.add_airport(essendon)
#melbourne.add_airport(avalon)

melbourne.add_hotel(lancemore_crossley)
melbourne.add_hotel(grand_hyatt_melbourne)
#melbourne.add_hotel(crown_metropol)

melbourne.add_turism(melbourne_zoo)
melbourne.add_turism(icebar)
#melbourne.add_turism(great_ocean_road)

washington = City('Washington', sku='C3')

washington.add_airport(ronald_reagan)
washington.add_airport(washington_dulles)
#washington.add_airport(baltimore_washington)

washington.add_hotel(grand_hyatt_washington)
washington.add_hotel(hilton_garden)
#washington.add_hotel(embassy_row)

washington.add_turism(pentagon)
washington.add_turism(white_house)
#washington.add_turism(smithsonians)

fez = City('Fez', sku='C4')

fez.add_airport(fez_saiss)
fez.add_airport(mohammed)
#fez.add_airport(muzayaf)

fez.add_hotel(palais_medina)
fez.add_hotel(dar_tahri)
#fez.add_hotel(zalagh_parc_palace)

fez.add_turism(blue_city)
fez.add_turism(la_medina_tour)
#fez.add_turism(desert_tour)

paris = City('Paris', sku='C5')

paris.add_airport(charles_de_gaulle)
paris.add_airport(orly)
#paris.add_airport(beauvais_tille)

paris.add_hotel(balzac)
paris.add_hotel(intercontinental_le_grand)
#paris.add_hotel(renaissance_paris)

paris.add_turism(eiffel_tower)
paris.add_turism(louvre)
#paris.add_turism(notre_dame)

pekin = City('Pekin', sku='C6')

pekin.add_airport(pekin_international)
pekin.add_airport(peking_daxing)
#pekin.add_airport(zhege_jichang)

pekin.add_hotel(grand_skylight)
pekin.add_hotel(beijing_jinjiang)
#pekin.add_hotel(sunworld_dynasty)

pekin.add_turism(great_wall)
pekin.add_turism(forbidden_city)
#pekin.add_turism(tiananmen)


cities = [
    santiago,
    melbourne,
    washington,
    fez,
    paris,
    pekin
]
