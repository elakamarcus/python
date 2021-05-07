#!/usr/bin/env python3
#
# mt19937.py - a quick and dirty implementation of the MT19937 PRNG in Python
#
#    Copyright (C) 2020  Tom Liston - email: tom.liston@bad-wolf-sec.com
#                                   - twitter: @tliston
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see [http://www.gnu.org/licenses/].

import random

# this is simply a python implementation of a standard Mersenne Twister PRNG.
# the parameters used, implement the MT19937 variant of the PRNG, based on the
# Mersenne prime 2^19937−1
# see https://en.wikipedia.org/wiki/Mersenne_Twister for a very good explanation
# of the math behind this...

class mt19937():
    u, d = 11, 0xFFFFFFFF
    s, b = 7, 0x9D2C5680
    t, c = 15, 0xEFC60000
    l = 18
    n = 624

    def my_int32(self, x):
        return(x & 0xFFFFFFFF)

    def __init__(self, seed):
        w = 32
        r = 31
        f = 1812433253
        self.m = 397
        self.a = 0x9908B0DF
        self.MT = [0] * self.n
        self.index = self.n + 1
        self.lower_mask = (1 << r) - 1
        self.upper_mask = self.my_int32(~self.lower_mask)
        self.MT[0] = self.my_int32(seed)
        for i in range(1, self.n):
            self.MT[i] = self.my_int32((f * (self.MT[i - 1] ^ (self.MT[i - 1] >> (w - 2))) + i))

    def extract_number(self):
        if self.index >= self.n:
            self.twist()
            self.index = 0
        y = self.MT[self.index]
        # this implements the so-called "tempering matrix"
        # this, functionally, should alter the output to
        # provide a better, higher-dimensional distribution
        # of the most significant bits in the numbers extracted
        y = y ^ ((y >> self.u) & self.d)
        y = y ^ ((y << self.s) & self.b)
        y = y ^ ((y << self.t) & self.c)
        y = y ^ (y >> self.l)
        self.index += 1
        return self.my_int32(y)

    def twist(self):
        for i in range(0, self.n):
            x = (self.MT[i] & self.upper_mask) + (self.MT[(i + 1) % self.n] & self.lower_mask)
            xA = x >> 1
            if(x % 2) != 0:
                xA = xA ^ self.a
            self.MT[i] = self.MT[(i + self.m) % self.n] ^ xA


# so... guess what! while it isn't necessarily obvious, the
# functioning of the tempering matrix are mathematically
# reversible. this function impliments that...
#
# by using this, we can take the output of the MT PRNG, and turn
# it back into the actual values held within the MT[] array itself
# and therefore, we can "clone" the state of the PRNG from "n"
# generated random numbers...
#
# initially, figuring out the math to do this made my brain hurt.
# simplifying it caused even more pain.
# please don't ask me to explain it...
def untemper(y):
    y ^= y >> mt19937.l
    y ^= y << mt19937.t & mt19937.c
    for i in range(7):
        y ^= y << mt19937.s & mt19937.b
    for i in range(3):
        y ^= y >> mt19937.u & mt19937.d
    return y


if __name__ == "__main__":

    # snowball fight numbers:
    snowballs = [60139882, 1207682830, 3939072931, 153605103, 3769185122, 3210606542, 396585332, 2301957203, 453350119, 63226260, 352199818,
    2196110054, 805610298, 3346968699, 101499007, 2576708619, 892755958, 2651747964, 870747414,3713406335, 3494989727,1923472825, 2337519438,
    707517923, 47281812, 121199962,3736389373,2831247838,2657725673,2703371777, 1916315088, 3940358194,3419873702,
    470847769, 761689665, 3164156510, 3258641831, 3964563224,3648151005,2318335003, 44531568,3176921177,2656140082, 2229541206,
    890621450,
    1181609158,
    721884446,
    1638416881,
    2334614612,
    1426915432,
    3372620563,
    2254133934,
    352793831,
    179887204,
    429049387,
    3933404091,
    3610704691,
    1988144249,
    3884171684,
    3034086305,
    731594409,
    1686434392,
    566984981,
    236544716,
    1717967738,
    2929631550,
    3387746382,
    1122533313,
    1528505082,
    983091717,
    2663978619,
    2142399298,
    2894401684,
    2532989081,
    2225517842,
    1045594688,
    2687534098,
    1619056748,
    1777616502,
    234173533,
    2476756253,
    228555257,
    2596323350,
    3203080535,
    3110792254,
    3192063405,
    2919290609,
    833430880,
    1156134754,
    1326228663,
    3501912785,
    968333315,
    2951670659,
    4089031239,
    1741934406,
    2737017424,
    2435226627,
    625312373,
    2284303553,
    840519794,
    2893702658,
    1635693691,
    169980964,
    3504445790,
    3693868249,
    3276938971,
    2895625948,
    2774354273,
    37769197,
    563027285,
    1162954683,
    811539379,
    3149193777,
    70309286,
    3856035946,
    1893956710,
    3477038152,
    86145513,
    1008276108,
    1428167107,
    1786416891,
    318881277,
    4223760541,
    3570806130,
    3167752833,
    1607145072,
    168926042,
    2796397473,
    9920872,
    1281192602,
    88405337,
    3636882831,
    3382368999,
    1029920073,
    3346811106,
    3224475414,
    272230239,
    2567454097,
    2205410018,
    203215111,
    959980361,
    3714704968,
    1494041648,
    4131972374,
    3122844169,
    1089777441,
    2895458869,
    2580822063,
    1938847227,
    1420197575,
    2485064156,
    2987056553,
    2199414817,
    3239437014,
    3921984722,
    2791055703,
    1072148102,
    3380412901,
    2136710715,
    199560374,
    1241487373,
    3141019076,
    1400051666,
    2020355714,
    1342407216,
    1074050809,
    3082907679,
    2602211333,
    3628129,
    776501052,
    743166668,
    2217035061,
    3247732281,
    3368307909,
    1047756171,
    3318465547,
    2005871618,
    2421291984,
    527318629,
    4023223289,
    4001547326,
    1722459661,
    2415227668,
    3676588298,
    1226578071,
    227314821,
    2397223451,
    2267952140,
    2922921926,
    804111317,
    2426212738,
    2491200681,
    1571158905,
    2326413198,
    1468928729,
    432139708,
    2387816875,
    3525067369,
    1656906208,
    2395749390,
    965618779,
    237198903,
    2976584480,
    4124024884,
    2773599017,
    3373331164,
    3223492422,
    2860656380,
    2029291435,
    558792031,
    1540613957,
    3865740777,
    2576431888,
    3436781883,
    2264142882,
    873346949,
    2030309634,
    1363664261,
    786671749,
    1346230269,
    780776532,
    2744102446,
    2951883493,
    182585733,
    1304807486,
    1041109802,
    1784679956,
    3893618803,
    3923739447,
    2838841853,
    1194843709,
    3195373987,
    1262392144,
    619882777,
    98533349,
    3170295289,
    3474833829,
    4104751137,
    1764882709,
    384130929,
    732215420,
    2333555653,
    3533113143,
    2882055626,
    2506636451,
    3958814392,
    1934694387,
    203490108,
    627742835,
    854676385,
    2194748485,
    53049876,
    3801648584,
    3690207002,
    1487638070,
    836225471,
    1083954578,
    273720859,
    2391814981,
    2619026762,
    547123109,
    83626172,
    3759752796,
    2638336250,
    2588778750,
    1612562249,
    3013682368,
    723993638,
    3414200831,
    69827286,
    3679134944,
    4083799684,
    3669731798,
    2538486023,
    1459980098,
    4012263997,
    2793196328,
    1255680792,
    2373894934,
    1438080323,
    2780560608,
    1643744953,
    3931345567,
    1717245623,
    1253610915,
    2686538863,
    216102311,
    3233958959,
    2592326543,
    3644003568,
    581883313,
    947997990,
    2044088301,
    3365587446,
    2104842776,
    273880121,
    2031388987,
    1277896467,
    3689793204,
    526555389,
    1152164417,
    558715093,
    2575879201,
    3512946188,
    2783460966,
    1419859974,
    379945788,
    4062737284,
    1047300678,
    3464346541,
    688416362,
    973673641,
    2028776688,
    104618661,
    2221120809,
    1850247445,
    2992188403,
    4143449954,
    1858825518,
    3571644876,
    3737758580,
    153579224,
    3762634313,
    4016903050,
    644205610,
    3992027925,
    1478342931,
    2812741268,
    2617217774,
    1692652494,
    2882706444,
    757535175,
    2751450135,
    3070873303,
    2555600292,
    3872040083,
    3470539933,
    1788720383,
    2397787540,
    2862150974,
    1262037069,
    2310441739,
    1270324172,
    3562545491,
    2733605280,
    905443323,
    577856315,
    2108628081,
    2471816993,
    2792903464,
    1067157160,
    461184149,
    2055651696,
    2260073498,
    2115841694,
    1481465068,
    1728732334,
    94504342,
    953693927,
    251226029,
    3656853379,
    1385624048,
    724332552,
    1819515528,
    2634411676,
    3756691180,
    2897938528,
    3704578059,
    1650303487,
    2468856935,
    1706866501,
    418379324,
    3409761686,
    2468155595,
    1183183706,
    1068695988,
    3859651786,
    3147162500,
    3495551305,
    3517411847,
    207927065,
    3028085987,
    1158869479,
    3858767008,
    4174978247,
    2103580333,
    3630330663,
    3172163279,
    3850065249,
    2033879871,
    1070589671,
    3400858900,
    2391467923,
    1642158817,
    18522370,
    1925940955,
    1832939847,
    3034041075,
    958596312,
    3285036972,
    352000117,
    2401365691,
    3794110768,
    266229383,
    3028688394,
    3832548033,
    409198271,
    1573045935,
    4143201553,
    265224317,
    893353160,
    1580470336,
    2515872032,
    3208325910,
    2746495136,
    2098968,
    3336485639,
    2292025762,
    1134471635,
    3261185200,
    3003216409,
    744490170,
    486066548,
    1749830643,
    286732756,
    3779905703,
    2129230405,
    3666094048,
    3536005485,
    34587341,
    3607214240,
    3538288812,
    1343893611,
    3884183184,
    4250710723,
    1256912438,
    4112983421,
    2280947129,
    3681864083,
    1027962434,
    912283795,
    1325593906,
    631959087,
    2655763681,
    833546107,
    543903193,
    2318286263,
    2468962811,
    4123501650,
    1861363244,
    1045733329,
    1623832990,
    1994197895,
    940156544,
    917919133,
    2669668503,
    1054408116,
    3781048142,
    3944500407,
    1539742199,
    651224002,
    1212823388,
    4206061664,
    1716481147,
    4231281246,
    1172795688,
    3398423270,
    139148582,
    1608881328,
    552375916,
    3552411726,
    2569056643,
    274961179,
    1079938789,
    4226962513,
    3136584958,
    3795275919,
    1510671946,
    384877773,
    3568425339,
    1243223247,
    3931876768,
    3784492752,
    279908539,
    560013988,
    2812324578,
    3862937380,
    3614691421,
    1917804702,
    425110223,
    66463182,
    2913965564,
    1651190090,
    3005507643,
    1975146211,
    1070402551,
    2709008291,
    2946892231,
    2562283851,
    3285396117,
    520245722,
    1103726468,
    2249975543,
    2281865560,
    887020790,
    1566493825,
    679223316,
    3009239578,
    1111775752,
    3409824277,
    3497091328,
    873667667,
    1529022102,
    2650715840,
    1189280444,
    901849322,
    2685323396,
    2115401903,
    1286595902,
    3501270,
    1903295167,
    3869290104,
    1877507738,
    1685345551,
    990560197,
    2140162919,
    2418223179,
    658948936,
    1182047475,
    2586262116,
    2214572174,
    1227235618,
    2826810043,
    613676688,
    3077712499,
    4110139247,
    3450501932,
    2973091588,
    1479213639,
    1692237477,
    1258995160,
    2729420354,
    2187733576,
    3869132451,
    2605302324,
    2140501890,
    4183569042,
    2202705280,
    3851283904,
    825269306,
    791068578,
    262558883,
    1783850381,
    1523211357,
    4130156813,
    3221044418,
    3018965083,
    741674399,
    2702672836,
    3948491807,
    2276849756,
    452651131,
    104635918,
    1041473245,
    3393530001,
    3504578177,
    2318149675,
    876078445,
    1233424183,
    1509685767,
    1252204710,
    3805013503,
    3972525855,
    4072067037,
    2519937393,
    423654155,
    3704667751,
    3527444342,
    2146772554,
    1368769930,
    746730785,
    2793596761,
    97373757,
    2212486869,
    843364042,
    1380026571,
    289149461,
    2816035170,
    3421376762,
    542587008,
    1743910098,
    3406480011,
    757339097,
    1584048341,
    3317786631,
    1809105032,
    2927436233,
    3284028660,
    1667792913,
    1400846097,
    2664476591,
    4287423067,
    98916468,
    1966349450,
    1200146432,
    3972868353,
    2427431251,
    2545223213,
    1605219271,
    160151252,
    1210696427,
    372767880,
    372544304,
    3863212196,
    2252294886,
    4248921911, 235818564, 2542110854, 3355836556, 1525036101, 373762821, 2087298533,3569492636, 2874540172]

    # create our own version of an MT19937 PRNG.
    myprng = mt19937(0)
    # fire up Python's built-in PRNG and seed it with the time...
    print("Seeding Python's built-in PRNG with the time...")
    random.seed()
    # generate some random numbers so we can create a random number of random numbers using Python's built-in PRNG
    # so random...
    count1 = random.randint(2000, 10000)
    #count2 = random.randint(2000, 10000)
    count2 = len(snowballs)
    print("Generating a random number (%i) of random numbers using Python's built-in PRNG..." % (count1))
    print("We do this just to show that this method doesn't depend on being at a particular starting point.")
    for i in range(count1):
        f = random.randrange(0xFFFFFFFF)
    # clone that sucker...
    print("Generating %i random numbers.\nWe'll use those values to create a clone of the current state of Python's built-in PRNG..." % (mt19937.n))
    for i in range(mt19937.n):
        myprng.MT[i] = untemper(random.randrange(0xFFFFFFFF))
    # check to make sure our cloning worked...
    print("Generating a random number (%i) of additional random numbers using Python's built-in PRNG..." % (count2))
    print("Generating those %i random numbers with our clone as well..." % (count2))
    # generate numbers and throw 'em away...
    for i in range(count2):
        f = random.randrange(0xFFFFFFFF)
        f2 = myprng.extract_number()
    print("Now, we'll test the clone...")
    print("\nPython       Our clone")
    for i in range(20):
        r1 = random.randrange(0xFFFFFFFF)
        r2 = myprng.extract_number()
        print("%10.10i - %10.10i (%r)" % (r1, r2, (r1 == r2)))
        assert(r1 == r2)