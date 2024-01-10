# VEP proposal for IVOA RefFrame vocabulary

**Vocabulary**: http://www.ivoa.net/rdf/refframe
**Author**: Baptiste Cecconi <baptiste.cecconi@obspm.fr>
**Date**: 2023-11-10
______________________________________________________________

**Term**: `#67PCG_CSO`
**Label**: Comet solar orbital centered on comet 67P
**Definition**: 
The 67P Comet solar orbital frame is defined as a two-vector style dynamic frames as follows:
-  The position of the sun relative to 67P is the primary vector: the X axis points from the comet to the sun.
-  The inertially referenced velocity of the sun relative to 67P is the secondary vector: the Y axis is the component of this velocity vector orthogonal to the X axis.
-  The Z axis is X cross Y, completing the right-handed reference frame.
______________________________________________________________

**Term**: `#67PCG_EME`
**Label**: J2000 centered on comet 67P
**Definition**:
Same as `#EME`, but centered on comet 67P Churyumov-Gerasimenko.
______________________________________________________________

**Term**: `#CPHIO`
**Label**:  Callisto Phi-Omega
**Definition**:
In this Cartesian coordinate system, X is along the flow direction, Y is along the Callisto-Jupiter vector, and Z is along the spin axis.

These coordinates are analogous to the earth-centered GSE coordinates that relate to the direction of flow of the solar wind onto Earth's environment 

______________________________________________________________

**Term**: `#DIIS`
**Label**:  Dione Inter-action coordinate System
**Definition**:
The Moon Inter-action coordinate System frame is defined as follows:
-  The inertially referenced velocity of Saturn relative to Dione is the primary vector: +X;
-  The position of Saturn relative to Dione is the secondary vector: +Y axis points from Dione to Saturn;
-  +Z axis completes the right-handed system;
-  the origin of this frame is Dione's center of mass.
______________________________________________________________

**Term**: `#DME`
**Label**: Deimos Mean Equator
**Definition**:
The Deimos Mean Equator of Date frame (also known as Deimos Mean Equator and IAU vector of Date frame) is defined as follows :
-  X-Y plane is defined by the Deimos equator of date, and the +Z axis, primary vector of this frame, is parallel to the Moon's rotation axis of date, pointing toward the North side of the invariant plane;
-  +X axis is defined by the intersection of the Moon's equator of date with the Earth Mean Equator of J2000;
-  +Y axis completes the right-handed system;
-  the origin of this frame is Deimos' center of mass.
______________________________________________________________

**Term**: `#DSE`
**Label**: Deimos-centric Solar Ecliptic
**Definition**:
The Deimos-centric Solar Ecliptic frame is defined as follows:
-  The position of the Sun relative to Deimos is the primary vector: +X axis points from Moon to the Sun;
-  The inertially referenced velocity of the Sun relative to Deimos is the secondary vector: +Y axis is the component of this velocity vector orthogonal to the +X axis;
-  +Z axis completes the right-handed system;
-  the origin of this frame is Deimos' center of mass.
______________________________________________________________

**Term**: `#ECLIPDATE`
**Label**: Earth Mean Ecliptic and Equinox
**Definition**:
The Earth Mean Ecliptic and Equinox of Date frame is defined as follows:
- +Z axis is aligned with the north-pointing vector normal to the mean orbital plane of the Earth;
- +X axis points along the ''mean equinox'', which is defined as the intersection of the Earth's mean orbital plane with the Earth's mean equatorial plane. It is aligned with the cross product of the north-pointing vectors normal to the Earth's mean equator and mean orbit plane of date;
- +Y axis is the cross product of the Z and X axes and completes the right-handed frame;
-  the origin of this frame is the Earth's center of mass.

The mathematical model used to obtain the orientation of the Earth's mean equator and equinox of date frame is the 1976 IAU precession model, built into SPICE.

The mathematical model used to obtain the mean orbital plane of the Earth is the 1980 IAU obliquity model, also built into SPICE.

The base frame for the 1976 IAU precession model is J2000.
______________________________________________________________

**Term**: `#ECLIPJ2000`
**Label**: Ecliptic coordinates based upon the J2000 frame
**Definition**:
The value for the obliquity of the ecliptic at J2000 is taken from of 'Explanatory Supplement to the Astronomical Almanac' edited by P. Kenneth Seidelmann. University Science Books, 20 Edgehill Road, Mill Valley, CA 94941 (1992) page 114 equation 3.222-1
______________________________________________________________

**Term**: `#EME`
**Label**: Earth Mean Equator and Equinox
**Description**: 
The Earth Mean Equator and Equinox of Date frame is defined as follows:
-  +Z axis is aligned with the north-pointing vector normal to the mean equatorial plane of the Earth;
-  +X axis points along the ''mean equinox'', which is defined as the intersection of the Earth's mean orbital plane with the Earth's mean equatorial plane. It is aligned with the cross product of the north-pointing vectors normal to the Earth's mean equator and mean orbit plane of date;
-  +Y axis is the cross product of the Z and X axes and completes the right-handed frame;
-  the origin of this frame is the Earth's center of mass.
______________________________________________________________

**Term**: `#ENIS`
**Label**: Enceladus Inter-action coordinate System
**Definition**: 
The Moon Inter-action coordinate System frame is defined as follows:
-  The inertially referenced velocity of Saturn relative to Enceladus is the primary vector: +X;
-  The position of Saturn relative to Enceladus is the secondary vector: +Y axis points from Moon to Saturn;
-  +Z axis completes the right-handed system;
-  the origin of this frame is Enceladus' center of mass.
______________________________________________________________

**Term**: `#EPHIO`
**Label**: Europa Phi-Omega
**Definition**: 
In this Cartesian coordinate system, X is along the flow direction, Y is along the Europa-Jupiter vector, and Z is along the spin axis.

These coordinates are analogous to the earth-centered GSE coordinates that relate to the direction of flow of the solar wind onto Earth's environment 

______________________________________________________________

**Term**: `#GPHIO`
**Label**: Ganymede Phi-Omega
**Definition**:
In this Cartesian coordinate system, X is along the flow direction, Y is along the Ganymede-Jupiter vector, and Z is along the spin axis.

These coordinates are analogous to the earth-centered GSE coordinates that relate to the direction of flow of the solar wind onto Earth's environment 

______________________________________________________________

**Term**: `#GRIGGSKELL_CSO`
**Label**: Comet solar orbital centered on GRIGG-SKJELLERUP comet
**Definition**:
GRIGG-SKJELLERUP Solar Orbital frame is defined as a two-vector style dynamic frames as follows:
-  The position of the sun relative to the comet is the primary vector: the X axis points from the comet to the sun.
-  The inertially referenced velocity of the sun relative to the comet is the secondary vector: the Y axis is the component of this velocity vector orthogonal to the X axis.
-  The Z axis is X cross Y, completing the right-handed reference frame.
         
______________________________________________________________

**Term**: `#GRIGGSKELL_EME`
**Label** J2000 centered on GRIGG-SKJELLERUP comet
**Definition**: 
Same as `#EME` (Earth mean equator, dynamical equinox of J2000) but centered on GRIGG-SKJELLERUP.
______________________________________________________________

**Term**: `#GSE` 
**Label**: Geocentric Solar Ecliptic
**Definition**: 
The Earth-centric Solar Ecliptic frame is defined as follows :
-  X-Y plane is defined by the Earth Mean Ecliptic plane of date: the +Z axis, primary vector, is the normal vector to this plane, always pointing toward the North side of the invariant plane;
-  +X axis is the component of the Earth-Sun vector that is orthogonal to the +Z axis;
-  +Y axis completes the right-handed system;
-  the origin of this frame is the Sun's center of mass.
______________________________________________________________

**Term**: `#GSEQ`
**Label**: Geocentric Solar Equatorial
**Definition**: 
The Geocentric Solar Equatorial frame is defined as follows :
- +X axis is the position of the Sun relative to the Earth; it's the primary vector and points from the Earth to the Sun;
- +Z axis is the component of the Sun's north pole of date orthogonal to the +X axis;
- +Y axis completes the right-handed reference frame;
- the origin of this frame is the Earth's center of mass.
______________________________________________________________

**Term**: `#GSM`
**Label**: Geocentric Solar Magnetospheric
**Definition**:
A coordinate system where the X axis is from Earth to Sun, Z axis is northward in a plane containing the X axis and the geomagnetic dipole axis. See Russell, 1971

Thus, +X is identical to `#GSE` +X and is the primary, and +Z is the secondary and is the MAG +Z.
______________________________________________________________

**Term**: `#HALLEY_CSO`
**Label**: Comet solar orbital centered on HALLEY comet
**Definition**:
Halley comeet solar orbital frame is defined as a two-vector style dynamic frames as follows:
-  The position of the sun relative to the comet is the primary
vector: the X axis points from the comet to the sun.
-  The inertially referenced velocity of the sun relative to the comet is the secondary vector: the Y axis is the component of this velocity vector orthogonal to the X axis.
-  The Z axis is X cross Y, completing the right-handed reference frame.
______________________________________________________________

**Term**: `#HALLEY_EME`
**Label**: J2000 centered on HALLEY comet
**Definition**: 
Same as `#EME` (Earth mean equator, dynamical equinox of J2000) but centered on Halley comet.

______________________________________________________________

**Term**: `#HCI`
**Label**: Heliocentric Inertial
**Definition**: 
The Heliocentric Inertial Frame is defined as follows :
- X-Y plane is defined by the Sun's equator of epoch J2000: the +Z axis, primary vector, is parallel to the Sun's rotation axis of epoch J2000, pointing toward the Sun's north pole;
- +X axis is defined by the ascending node of the Sun's equatorial plane on the ecliptic plane of J2000;
- +Y completes the right-handed frame;
- the origin of this frame is the Sun's center of mass.
______________________________________________________________

**Term**: `#HEE` 
**Label**: Heliocentric Earth Ecliptic
**Definition**: 
The Heliocentric Earth Ecliptic frame is defined as follows :
-  X-Y plane is defined by the Earth Mean Ecliptic plane of date, therefore, the +Z axis is the primary vector,and it defined as the normal vector to the Ecliptic plane that points toward the north pole of date;
-  +X axis is the component of the Sun-Earth vector that is orthogonal to the +Z axis;
-  +Y axis completes the right-handed system;
-  the origin of this frame is the Sun's center of mass.
______________________________________________________________

**Term**: `#HEEQ` 
**Labem**: Heliocentric Earth Equatorial
**Definition**: 
The Heliocentric Earth Equatorial frame is defined as follows:
- X-Y plane is the solar equator of date, therefore, the +Z axis is the primary vector and it is aligned to the Sun's north pole of date;
- +X axis is defined by the intersection between the Sun equatorial plane and the solar central meridian of date as seen from the Earth. The solar central meridian of date is defined as the meridian of the Sun that is turned toward the Earth. Therefore, +X axis is the component of the Sun-Earth vector that is orthogonal to the +Z axis;
- +Y axis completes the right-handed system;
- the origin of this frame is the Sun's center of mass.
______________________________________________________________

**Term**: `#IAU_EARTH` 
**Label**: Earth-centered Body-Fixed Frame
**Definition**: 
IAU Frame for the Earth. 
*Reference*: Archinal, B.A., Acton, C.H., A’Hearn, M.F. et al. Report of the IAU Working Group on Cartographic Coordinates and Rotational Elements: 2015. Celest Mech Dyn Astr 130, 22 (2018). https://doi.org/10.1007/s10569-017-9805-5

______________________________________________________________

**Term**: `#IAU_JUPITER`
**Label**: Jupiter-centered Body-Fixed Frame
**Definition**: 
IAU Frame for Jupiter. 
*Reference*: Archinal, B.A., Acton, C.H., A’Hearn, M.F. et al. Report of the IAU Working Group on Cartographic Coordinates and Rotational Elements: 2015. Celest Mech Dyn Astr 130, 22 (2018). https://doi.org/10.1007/s10569-017-9805-5

______________________________________________________________

**Term**: `#IAU_MARS`
**Label**: Mars-centered Body-Fixed Frame
**Definition**: 
IAU Frame for Mars. 
*Reference*: Archinal, B.A., Acton, C.H., A’Hearn, M.F. et al. Report of the IAU Working Group on Cartographic Coordinates and Rotational Elements: 2015. Celest Mech Dyn Astr 130, 22 (2018). https://doi.org/10.1007/s10569-017-9805-5

______________________________________________________________

**Term**: `#IAU_MERCURY` 
**Label**: Mercury-centered Body-Fixed Frame
**Definition**:
IAU Frame for Mercury. 
*Reference*: Archinal, B.A., Acton, C.H., A’Hearn, M.F. et al. Report of the IAU Working Group on Cartographic Coordinates and Rotational Elements: 2015. Celest Mech Dyn Astr 130, 22 (2018). https://doi.org/10.1007/s10569-017-9805-5

______________________________________________________________

**Term**: `#IAU_MOON`
**Label**: Moon-Centered Body-Fixed Frame
**Definition**: 
IAU Frame for the Moon (Earth natural satellite). 
*Reference*: Archinal, B.A., Acton, C.H., A’Hearn, M.F. et al. Report of the IAU Working Group on Cartographic Coordinates and Rotational Elements: 2015. Celest Mech Dyn Astr 130, 22 (2018). https://doi.org/10.1007/s10569-017-9805-5

______________________________________________________________

**Term**: `#IAU_NEPTUNE` 
**Label**: Neptune-centered Body-Fixed Frame
**Definition**:
IAU Frame for Neptune. 
*Reference*: Archinal, B.A., Acton, C.H., A’Hearn, M.F. et al. Report of the IAU Working Group on Cartographic Coordinates and Rotational Elements: 2015. Celest Mech Dyn Astr 130, 22 (2018). https://doi.org/10.1007/s10569-017-9805-5

______________________________________________________________

**Term**: `#IAU_PLUTO`
**Label**: Pluto-centered Body-Fixed Frame
**Definition**: 
IAU Frame for Pluto. 
*Reference*: Archinal, B.A., Acton, C.H., A’Hearn, M.F. et al. Report of the IAU Working Group on Cartographic Coordinates and Rotational Elements: 2015. Celest Mech Dyn Astr 130, 22 (2018). https://doi.org/10.1007/s10569-017-9805-5

______________________________________________________________

**Term**: `#IAU_SATURN`
**Label**: Saturn-centered Body-Fixed Frame
**Definition**: 
IAU Frame for Saturn. 
*Reference*: Archinal, B.A., Acton, C.H., A’Hearn, M.F. et al. Report of the IAU Working Group on Cartographic Coordinates and Rotational Elements: 2015. Celest Mech Dyn Astr 130, 22 (2018). https://doi.org/10.1007/s10569-017-9805-5

______________________________________________________________

**Term**: `#IAU_SUN`
**Label**: Sun-centered Body-Fixed Frame
**Definition**:
IAU Frame for the Sun. 
*Reference*: Archinal, B.A., Acton, C.H., A’Hearn, M.F. et al. Report of the IAU Working Group on Cartographic Coordinates and Rotational Elements: 2015. Celest Mech Dyn Astr 130, 22 (2018). https://doi.org/10.1007/s10569-017-9805-5
______________________________________________________________

**Term**: `#IAU_URANUS`
**Label**: Uranus-centered Body-Fixed Frame
**Definition**: 
IAU Frame for Uranus. 
*Reference*: Archinal, B.A., Acton, C.H., A’Hearn, M.F. et al. Report of the IAU Working Group on Cartographic Coordinates and Rotational Elements: 2015. Celest Mech Dyn Astr 130, 22 (2018). https://doi.org/10.1007/s10569-017-9805-5

______________________________________________________________

**Term**: `#IAU_VENUS`
**Label**: Venus-centered Body-Fixed Frame
**Definition**: 
IAU Frame for Venus. 
*Reference*: Archinal, B.A., Acton, C.H., A’Hearn, M.F. et al. Report of the IAU Working Group on Cartographic Coordinates and Rotational Elements: 2015. Celest Mech Dyn Astr 130, 22 (2018). https://doi.org/10.1007/s10569-017-9805-5

______________________________________________________________

**Term**: `#IPHIO`
**Label**: Io Phi-Omega
**Definition**:
In this Cartesian coordinate system, X is along the flow direction, Y is along the Io-Jupiter vector, and Z is along the spin axis.

These coordinates are analogous to the earth-centered GSE coordinates that relate to the direction of flow of the solar wind onto Earth's environment 
______________________________________________________________

**Term**: `#J2000`
**Label**: Earth mean equator, dynamical equinox of J2000
**Definition**: 
Earth mean equator, dynamical equinox of J2000.

______________________________________________________________

**Term**: `#JECLIP`
**Label**: ECLIPJ2000 centered on Jupiter
**Definition**: 
Same as `#ECLIPJ2000` but centered on Jupiter.
The value for the obliquity of the ecliptic at J2000 is taken from of 'Explanatory Supplement to the Astronomical Almanac' edited by P. Kenneth Seidelmann. University Science Books, 20 Edgehill Road, Mill Valley, CA 94941 (1992) page 114 equation 3.222-1
______________________________________________________________

**Term**: `#JEME`
**Label**: J2000 centered on Jupiter
**Definition**:
Same as `#EME` (Earth mean equator, dynamical equinox of J2000), but centered on Jupiter

______________________________________________________________

**Term**: `#JSM`
**Label**: Jovian Solar Magnetospheric
**Definition**:
A coordinate system where the X axis is from Jupiter to Sun, Z axis is northward in a plane containing the X axis and the Jovian dipole axis.

Dipole is 159 longitude and 80 latitude.
______________________________________________________________

**Term**: `#JSO`
**Label**: Jovian Solar Orbital
**Definition**:
The Jupiter Solar Orbital frame is defined as follows:
-  The position of the Sun relative to Jupiter is the primary vector: +X axis points from Jupiter to the Sun;
-  The inertially referenced velocity of the Sun relative to Jupiter is the secondary vector: +Y axis is the component of this velocity vector orthogonal to the +X axis;
-  +Z axis completes the right-handed system;
-  the origin of this frame is Jupiter center of mass.
______________________________________________________________

**Term**: `#KECLIP`
**Label**: ECLIPJ2000 centered on Saturn
**Definition**:
Same as `#ECLIPJ2000` but centered on Saturn.
The value for the obliquity of the ecliptic at J2000 is taken from of 'Explanatory Supplement to the Astronomical Almanac' edited by P. Kenneth Seidelmann. University Science Books, 20 Edgehill Road, Mill Valley, CA 94941 (1992) page 114 equation 3.222-1

______________________________________________________________

**Term**: `#KEME` 
**Label**: J2000 centered on Saturn
**Definition**: 
Same as `#EME` (Earth mean equator, dynamical equinox of J2000), but centered on Saturn

______________________________________________________________

**Term**: `#KSM`
**Label**: Kronian Solar Magnetospheric
**Definition**: 
A coordinate system where the X axis is from Saturn to Sun, Z axis is northward in a plane containing the X axis and the Kronian dipole axis.

NB: Some sources refers magnetic dipole at 180 degrees longitude, 89.99 degrees latitude in the `#IAU_SATURN` frame. Other source make assume that the dipole axis is parallel to the spin axis.
______________________________________________________________

**Term**: `#KSO`
**Label**: Kronian Solar Orbital
**Definition**:
The Saturn Solar Orbital frame is defined as follows:
-  The position of the Sun relative to Saturn is the primary vector: +X axis points from Saturn to the Sun;
-  The inertially referenced velocity of the Sun relative to Saturn is the secondary vector: +Y axis is the component of this velocity vector orthogonal to the +X axis;
-  +Z axis completes the right-handed system;
-  the origin of this frame is Saturn center of mass.
______________________________________________________________

**Term**: `#LME`
**Label**: Moon Mean Equator
**Definition**: 
The Moon Mean Equator of Date frame (also known as Moon Mean Equator and IAU vector of Date frame) is defined as follows :
- X-Y plane is defined by the Moon equator of date, and the +Z axis, primary vector of this frame, is parallel to the Moon's rotation axis of date, pointing toward the North side of the invariant plane;
-  +X axis is defined by the intersection of the Moon's equator of date with the Earth Mean Equator of J2000;
- +Y axis completes the right-handed system;
-  the origin of this frame is Moon's center of mass.
______________________________________________________________

**Term**: `#LSE`
**Label**: Selenocentric Solar Ecliptic
**Definition**:
The Moon-centric Solar Ecliptic frame is defined as follows:
-  The position of the Sun relative to Moon is the primary vector: +X axis points from Moon to the Sun;
-  The inertially referenced velocity of the Sun relative to Moon is the secondary vector: +Y axis is the component of this velocity vector orthogonal to the +X axis;
-  +Z axis completes the right-handed system;
-  the origin of this frame is Moon's center of mass.
______________________________________________________________

**Term**: `#LUTETIA_CSO`
**Label**: Solar orbital centered on asteroid LUTETIA
**Definition**: 
Lutetia solar orbital frame is defined as a two-vector style dynamic frames as follows:
-  The position of the sun relative to the comet is the primary vector: the X axis points from the asteroid to the Sun.
-  The inertially referenced velocity of the sun relative to the asteroid is the secondary vector: the Y axis is the component of this velocity vector orthogonal to the X axis.
-  The Z axis is X cross Y, completing the right-handed reference frame.
______________________________________________________________

**Term**: `#LUTETIA_EME`
**Label**: J2000 centered on asteroid LUTETIA
**Definition**: 
Same as `#EME` (Earth mean equator, dynamical equinox of J2000) but centered on LUTETIA.
______________________________________________________________

**Term**: `#MAG`
**Label**: Geomagnetic coordinate system
**Definition**: 
MAG Frame definition from http://rbsp.space.umn.edu/data/rbsp/teams/spice/fk/rbsp_general011.tf


      Definition :

      Geomagnetic - geocentric. Z axis is parallel to the geomagnetic
      dipole axis, positive north. X is in the plane defined by the Z axis
      and the Earth's rotation axis. If N is a unit vector from the Earth's
      center to the north geographic pole, the signs of the X and Y axes are
      given by Y = N x Z, X = Y x Z.. See Russell, 1971
      

      The implementation of this frame is complicated in that the definition
      of the IGRF dipole is a function of time and the IGRF model cannot be
      directly incorporated into Spice. However, Spice does allow one to define
      time dependent Euler angles. Meaning, you can define an Euler angle
      that rotates GEO to MAG for a given ephemeris time t:

         V           = r(t) * V
          GEI                  MAG
      
      where r(t) is a time dependent Euler angle representation of a
      rotation. Spice allows for the time dependence to be represented by a
      polynomial expansion. This expansion can be fit using the IGRF model,
      thus representing the IGRF dipole axis.

      IGRF-11 (the 11th version) was fit for the period of 1990-2020, which
      should encompass the mission and will also make this kernel useful for
      performing Magnetic dipole frame transformations for the 1990's and
      the 2000's. However, IGRF-11 is not as accurate for this entire time
      interval. The years between 1945-2005 are labeled definitive, although
      only back to 1990 was used in the polynomial fit. 2005-2010 is
      provisional, and may change with IGRF-12. 2010-2015 was only a
      prediction. Beyond 2015, the predict is so far in the future as to not
      be valid. So to make the polynomials behave nicely in this region (in
      case someone does try to use this frame during that time), the
      2015 prediction was extended until 2020. So for low precision, this
      kernel can be used for the years 2015-2020. Any times less than 1990
      and greater than 2020 were not used in the fit, and therefore may be
      vastly incorrect as the polynomials may diverge outside of this region.
      These coefficients will be refit when IGRF-12 is released.
      
      Also, since the rest of the magnetic dipole frames are defined from
      this one, similar time ranges should be used for those frames.

                  Definitive           Provisional   Predict    Not Valid
       |------------------------------|+++++++++++|###########|???????????|
     1990                           2005        2010        2015        2020

      In addition to the error inherit in the model itself, the polynomial
      expansion cannot perfectly be fit the IGRF dipole. The maximum error
      on the fit is .2 milliradians, or .01 degrees. 

      The MAG frame is achieved by first rotating the GEO frame about Z by
      the longitude degrees, and then rotating about the Y axis by the
      amount of latitude. This matches the new frame to Russell's definition.
______________________________________________________________

**Term**: `#MECLIP`
**Label**: ECLIPJ2000 centered on Mercury
**Definition**: 
Same as `#ECLIPJ2000` but centered on Mercury.

The value for the obliquity of the ecliptic at J2000 is taken from of 'Explanatory Supplement to the Astronomical Almanac' edited by P. Kenneth Seidelmann. University Science Books, 20 Edgehill Road, Mill Valley, CA 94941 (1992) page 114 equation 3.222-1
______________________________________________________________

**Term**: `#MEME`
**Label**: J2000 centered on Mercury
**Definition**:
Same as `#EME` (Earth mean equator, dynamical equinox of J2000) but centered on Mercury.
______________________________________________________________

**Term**: `#MESE`
**Label**: Mercury-centric Solar Ecliptic
**Description**: 
The Mercury-centric Solar Ecliptic frame is defined as follows:
-  X-Y plane is defined by the Earth Mean Ecliptic plane of date: the +Z axis, primary vector, is the normal vector to this plane,always pointing toward the North side of the invariant plane;
-  +X axis is the component of the Mercury-Sun vector that is orthogonal to the +Z axis;
-  +Y axis completes the right-handed system;
-  the origin of this frame is the Sun's center of mass.
______________________________________________________________

**Term**: `#MESEQ`
**Label**: Mercury-centric Solar Equatorial
**Definition**: 
The Mercury-centric Solar Equatorial frame is defined as follows :
- +X axis is the position of the Sun relative to the Mercury; it's the primary vector and points from the Mercury to the Sun;
- +Z axis is the component of the Sun's north pole of date orthogonal to the +X axis;
- +Y axis completes the right-handed reference frame;
- the origin of this frame is the Mercury's center of mass.
______________________________________________________________

**Term**: `#MESO`
**Label**: Mercury-centric Solar Orbital
**Definition**: 
The Mercury Solar Orbital frame is defined as follows:
-  The position of the Sun relative to Mercury is the primary vector: +X axis points from Mercury to the Sun;
-  The inertially referenced velocity of the Sun relative to Mercury is the secondary vector: +Y axis is the component of this velocity vector orthogonal to the +X axis;
-  +Z axis completes the right-handed system;
-  the origin of this frame is Mercury center of mass.
______________________________________________________________

**Term**: `#MIIS`
**Label**: Mimas Inter-action coordinate System
**Definition**: 
The Mimas Inter-action coordinate System frame is defined as follows:
-  The inertially referenced velocity of Saturn relative to Mimas is the primary vector: +X;
-  The position of Saturn relative to Moon is the secondary vector: +Y axis points from Mimas to Saturn;
-  +Z axis completes the right-handed system;
-  the origin of this frame is Mimas' center of mass.
______________________________________________________________

**Term**: `#MME`
**Label**: Mars Mean Equator
**Definition**: 
The Mars Mean Equator of Date frame (also known as Mars Mean Equator and IAU vector of Date frame) is defined as follows :
- X-Y plane is defined by the Mars equator of date: the +Z axis, primary vector, is parallel to the Mars' rotation axis of date, pointing toward the North side of the invariant plane;
-  +X axis is defined by the intersection of the Mars' equator of date with the J2000 equator;
-  +Y axis completes the right-handed system;
-  the origin of this frame is Mars' center of mass.
______________________________________________________________

**Term**: `#MSO`
**Label**: Mars-centric Solar Orbital
**Definition**:
The Mars Solar Orbital frame is defined as follows:
- The position of the Sun relative to Mars is the primary vector: +X axis points from Mars to the Sun;
- The inertially referenced velocity of the Sun relative to Mars is the secondary vector: +Y axis is the component of this velocity vector orthogonal to the +X axis;
- +Z axis completes the right-handed system;
- the origin of this frame is Mars' center of mass.
______________________________________________________________

**Term**: `#NECLIP`
**Label**: ECLIPJ2000 centered on Neptune
**Definition**:
Same as `#ECLIPJ2000` but centered on Neptune.

The value for the obliquity of the ecliptic at J2000 is taken from of 'Explanatory Supplement to the Astronomical Almanac' edited by P. Kenneth Seidelmann. University Science Books, 20 Edgehill Road, Mill Valley, CA 94941 (1992) page 114 equation 3.222-1

______________________________________________________________

**Term**: `#NEME`
**Label**: J2000 centered on Neptune
**Definition**:
Same as `#EME` (Earth mean equator, dynamical equinox of J2000) but centered on Neptune.
______________________________________________________________

**Term**: `#NSO`
**Label**: Neptune-centric Solar Orbital Coordinates
**Definition**:
The Neptune Solar Orbital frame is defined as follows:
-  The position of the Sun relative to Neptune is the primary vector: +X axis points from Neptune to the Sun;
-  The inertially referenced velocity of the Sun relative to Neptune is the secondary vector: +Y axis is the component of this velocity vector orthogonal to the +X axis;
-  +Z axis completes the right-handed system;
-  the origin of this frame is Neptune center of mass.
______________________________________________________________

**Term**: `#PECLIP`
**Label**: ECLIPJ2000 centered on Pluto
**Definition**: 
Same as `#ECLIPJ2000` but centered on Pluto.

The value for the obliquity of the ecliptic at J2000 is taken from of 'Explanatory Supplement to the Astronomical Almanac' edited by P. Kenneth Seidelmann. University Science Books, 20 Edgehill Road, Mill Valley, CA 94941 (1992) page 114 equation 3.222-1
______________________________________________________________

**Term**: `#PEME`
**Label**: EME2000 centered on Pluto
**Definition**:
Same as `#EME`(Earth mean equator, dynamical equinox of J2000) but centered on Pluto.

______________________________________________________________

**Term**: `#PME`
**Label**: Phobos Mean Equator
**Definition**: 
The Phobos Mean Equator of Date frame (also known as Phobos Mean Equator and IAU vector of Date frame) is defined as follows :
-  X-Y plane is defined by the Phobos equator of date, and the +Z axis, primary vector of this frame, is parallel to the Moon's rotation axis of date, pointing toward the North side of the invariant plane;
-  +X axis is defined by the intersection of the Moon's equator of date with the Earth Mean Equator of J2000;
-  +Y axis completes the right-handed system;
-  the origin of this frame is Phobos' center of mass.
______________________________________________________________

**Term**: `#PSE`
**Label**: Phobos-centric Solar Ecliptic
**Definition**: 
The Phobos-centric Solar Ecliptic frame is defined as follows:
-  The position of the Sun relative to Phobos is the primary vector: +X axis points from Moon to the Sun;
-  The inertially referenced velocity of the Sun relative to Phobos is the secondary vector: +Y axis is the component of this velocity vector orthogonal to the +X axis;
-  +Z axis completes the right-handed system;
-  the origin of this frame is Phobos' center of mass.
______________________________________________________________

**Term**: `#PSO`
**Label**: Pluto-centric Solar Orbital Coordinates
**Definition**: 
The Pluto Solar Orbital frame is defined as follows:
-  The position of the Sun relative to Pluto is the primary vector: +X axis points from Pluto to the Sun;
-  The inertially referenced velocity of the Sun relative to Pluto is the secondary vector: +Y axis is the component of this velocity vector orthogonal to the +X axis;
-  +Z axis completes the right-handed system;
-  the origin of this frame is Pluto center of mass.
______________________________________________________________

**Term**: `#RHIS`
**Label**: Rhea Inter-action coordinate System
**Definition**: 
The Rhea Inter-action coordinate System frame is defined as follows:
-  The inertially referenced velocity of Saturn relative to Rhea is the primary vector: +X;
-  The position of Saturn relative to Rhea is the secondary vector: +Y axis points from Rhea to Saturn;
-  +Z axis completes the right-handed system;
-  the origin of this frame is Rhea's center of mass.
______________________________________________________________

**Term**: `#RTN`
**Label**: Sun-Spaceraft coordinate system
**Definition**:
RTN Frame is defined as follows:
- R is positive from the Sun to the spacecraft.
- T is omega cross R, where omega is the sun spin axis.
- N is R cross T, which completes the right-handed system.
					
This frame assumes the instantaneous center is located at the Sun, and not the spacecraft. Further, the axes are associated with the normal X, Y, and Z in the following manner:
- R -> X
- T -> Y
- N -> Z
______________________________________________________________

**Term**: `#RTP`
**Label**: Planet-Spaceraft coordinate system
**Definition**: 
The RTP frame is defined as follows:
- R is positive from the Planet to the spacecraft.
- T is omega cross R, where omega is the planet spin axis.
- P is R cross T, which completes the right-handed system.
                     
                
This frame assumes the instantaneous center is located at planet and not the spacecraft. Further, the axes are associated with the normal X, Y, and Z in the following manner:
- R     -> X
- Theta -> Y
- Phi   -> Z
______________________________________________________________

**Term**: `#SM`
**Label**: Solar Magnetic coordinates
**Definition**: 
A geocentric coordinate system where the Z axis is northward along Earth's dipole axis, X axis is in plane of z axis and Earth-Sun line, positive sunward. See Russell, 1971.

Thus, this is much like `#GSM`, except that now the +Z axis is the primary, meaning it is parallel to the dipole vector, and +X is the secondary. Since the X-Z plane is the same as `#GSM`'s X-Z plane, the Y axis is the same as `#GSM`.
______________________________________________________________

**Term**: `#STEINS_CSO`
**Label**: Solar orbital centered on asteroid STEINS
**Definition**: 
Steins solar orbital frame is defined as a two-vector style dynamic frames as follows:
-  The position of the sun relative to the asteroid is the primary vector: the X axis points from the comet to the sun.
-  The inertially referenced velocity of the sun relative to the asteroid is the secondary vector: the Y axis is the component of this velocity vector orthogonal to the X axis.
-  The Z axis is X cross Y, completing the right-handed reference frame.
______________________________________________________________

**Term**: `#STEINS_EME`
**Label**: J2000 centered on asteroid STEINS
**Definition**: 
Same as `#EME` (Earth mean equator, dynamical equinox of J2000) but centered on STEINS.
______________________________________________________________

**Term**: `#SYSTEM_3` 
**Label**: Jupiter-centered Body-Fixed Frame
**Definition**: 
Same as `#IAU_JUPITER`. 
______________________________________________________________

**Term**: `#TEIS`
**Label**: Tethys Inter-action coordinate System
**Definition**: 
The Tethys Inter-action coordinate System frame is defined as follows:
-  The inertially referenced velocity of Saturn relative to Tethys is the primary vector: +X;
-  The position of Saturn relative to Moon is the secondary vector: +Y axis points from Tethys to Saturn;
-  +Z axis completes the right-handed system;
-  the origin of this frame is Tethys' center of mass.
______________________________________________________________

**Term**: `#TIIS`
**Label**: TItan Inter-action coordinate System
**Definition**:
The Titan Inter-action coordinate System frame is defined as follows:
-  The inertially referenced velocity of Saturn relative to Titan is the primary vector: +X;
-  The position of Saturn relative to Titan is the secondary vector: +Y axis points from Titan to Saturn;
-  +Z axis completes the right-handed system;
-  the origin of this frame is Titan's center of mass.
______________________________________________________________

**Term**: `#UECLIP`
**Label**: ECLIPJ2000 centered on Uranus
**Definition**:
Same as `#ECLIPJ2000` but centered on Uranus.

The value for the obliquity of the ecliptic at J2000 is taken from of 'Explanatory Supplement to the Astronomical Almanac' edited by P. Kenneth Seidelmann. University Science Books, 20 Edgehill Road, Mill Valley, CA 94941 (1992) page 114 equation 3.222-1
______________________________________________________________

**Term**: `#UEME`
**Label**: J2000 centered on Uranus
**Description**:
Same as `#EME`(Earth mean equator, dynamical equinox of J2000) but centered on Uranus.

______________________________________________________________

**Term**: `#USO`
**Label**: Uranus-centric Solar Orbital Coordinates
**Definition**:
The Uranus Solar Orbital frame is defined as follows:
-  The position of the Sun relative to Uranus is the primary vector: +X axis points from Uranus to the Sun;
-  The inertially referenced velocity of the Sun relative to Uranus is the secondary vector: +Y axis is the component of this velocity vector orthogonal to the +X axis;
-  +Z axis completes the right-handed system;
-  the origin of this frame is Uranus center of mass.
______________________________________________________________

**Term**: `#VME` 
**Label**: Venus Mean Equator
**Definition**:
The Venus Mean Equatorial of Date frame (also known as Venus Mean Equator and IAU vector of Date frame) is defined as follows :
- X-Y plane is defined by the Venus equator of date, and the +Z axis is parallel to the Venus' rotation axis of date, pointing toward the North side of the invariant plane;
- +X axis is defined by the intersection of the Venus' equator of date with the Earth Mean Equator of J2000;
- +Y axis completes the right-handed system;
-  the origin of this frame is Venus' center of mass.
______________________________________________________________

**Term**: `#VSO`
**Label**: Venus Solar Orbital
**Definition**: 
The Venus Solar Orbital frame is defined as follows:
-  The position of the Sun relative to Venus is the primary vector: +X axis points from Venus to the Sun;
-  The inertially referenced velocity of the Sun relative to Venus is the secondary vector: +Y axis is the component of this velocity vector orthogonal to the +X axis;
   +Z axis completes the right-handed system;
-  the origin of this frame is Venus center of mass.
______________________________________________________________

**Action**: Addition/Modification
**Used-in**: http://treps.cdpp.eu

**Rationale**: Extension of RefFrame for heliophysics (sun, solar wind and planetary plasma environments, magnetospheres, etc). This list  of terms allows to transform the CDPP/AMDA datasets into other scientifically useful frames. This list has been curated by the CDPP team. The terms of this list has be agreed with the IHDEA STCT working group.

NB: initial definition taken from: https://gitlab.irap.omp.eu/CDPP/TREPS/blob/master/server/kernel/data/frames.xml
