The following are notes on the GEI coordinate system.

There are two basic categories of the Geocentric Equatorial Inertial (GEI) coordinate frame in common use.

1. A non-inertial coordinate frame. There are several versions, depending on which how and which of the following time-varying effects are were accounted for
  * obliquity (tilt of the planetary rotation axis with respect to the ecliptic plane),
  * precession (rotation of planetary rotation axis tilt around the ecliptic pole),
  * nutation (perturbations to precession path), and
  * planetary precession (motion of the ecliptic with respect to the fixed starts).

2. An inertial coordinate frame. There are several versions that depend on how and which time-varying effects are accounted for but evaluate them at a specific date and time (epoch).

_Discuss why and when two versions are used._

# Terminology

The following terms are used in the references, and may need definition.

* Coordinate frame
* Coordinate representation
* Coordinate system
* True of Date
* Mean Equator
* Mean Equinox
* Mean Obliquity
* Ecliptic Plane
* Epoch is used to mean a reference date and time (an instant, rather than a period of time as is another common usage of "epoch")
* First point of Aries, i.e. vector(Earth-Sun)
* Vernal Equinox of Date

# Implementation Comparisons

Using [hxform](https://github.com/rweigel/hxform/), which wraps many libraries.

```
Time: [2010, 12, 30, 0, 0, 0]
Transform: GEI in car => GEO in car

                           x           y           z       magnitude
-----------------------------------------------------------------------------------
Input (GEI):           0.57735027  0.57735027  0.57735027  1.00000000

Output (GEO):                                                         ∠° wrt Input
-----------------------------------------------------------------------------------
cxform                 0.48763899 -0.65488540  0.57735027  1.00000000 76.30380821
geopack_08_dp          0.48765281 -0.65487510  0.57735027  1.00000000 76.30298692
spacepy                0.48759274 -0.65491984  0.57735027  1.00000000 76.30655535
spacepy-irbem          0.48765281 -0.65487510  0.57735027  1.00000000 76.30298692
spiceypy1              0.49005307 -0.65253584  0.57796623  1.00000000 76.12057248
spiceypy2              0.49005307 -0.65253584  0.57796623  1.00000000 76.12057248
sscweb                 0.49000000 -0.65000000  0.58000000  0.99949987 75.95945565
sunpy                  0.48938523 -0.65299116  0.57801786  1.00000000 76.15708166


max-min:               0.00246033  0.00491984  0.00264973  0.00050013  0.34709969°
100*|max-min|/|max|:       0.5021%     0.7569%     0.4569%     0.0500%     0.4549%
```

# [NAIF Tutorial](https://naif.jpl.nasa.gov/pub/naif/toolkit_docs/Tutorials/pdf/individual_docs/17_frames_and_coordinate_systems.pdf)

J2000 (also known as EME 2000, and is generally used in SPICE to refer to the ICRF)

The J2000* (aka EME2000) frame definition is based on the earth’s equator and equinox, determined from observations of planetary motions, plus other data.

*Caution: The name “J2000” is also used to refer to the zero epoch of the ephemeris time system (ET, also known as TDB)

The reference frame name "J2000" is generally used in SPICE as a label for the ICRF frame.

* In reality, any SPICE data said to be referenced to the J2000 frame are actually referenced to the ICRF frame.
  * Except for attitude derived from the 1976 IAU Earth precession model and 1980 IAU Earth nutation and mean obliquity of date models
* For historical and backwards compatibility reasons, only the name “J2000” is recognized by SPICE software as a frame name–not “ICRF.”

# [www.mssl.ucl.ac.uk](https://www.mssl.ucl.ac.uk/grid/iau/extra/local_copy/SP_coords/geo_sys.htm)

This system has its Z axis parallel to the Earth's rotation axis (positive to the North) and its X axis towards the First Point of Aries (the direction in space defined by the intersection between the Earth's equatorial plane and the plane of its orbit around the Sun (the plane of the ecliptic). This system is (to first order) fixed with respect to the distant stars. It is convenient for specifying the orbits (and hence location) of Earth-orbiting spacecraft as one can specify a Keplerian orbit in this frame.

However note that the GEI system is subject to second order change with time owing to the various slow motions of the Earth's rotation axis with respect to the fixed stars. Thus for GEI coordinates one must specify the date (normally termed the epoch) to which the coordinate system applies. For space physics work one should use the epoch-of-date GEI system, i.e. the system applying at the same time as the data were taken. (Thus the rotation axis in GEI is identical with the GEO rotation axis.) On these pages the unqualified acronym GEI refers to the epoch-of-date system. See Hapgood (1995) for a more detailed discussion of this issue.

# [SSCWeb](https://sscweb.gsfc.nasa.gov/users_guide/Appendix_C.shtml)

## GEI: Geocentric Equatorial Inertial system.

This system has X-axis pointing from the Earth toward the first point of Aries (the position of the Sun at the vernal equinox). This direction is the intersection of the Earth's equatorial plane and the ecliptic plane and thus the X-axis lies in both planes. The Z-axis is parallel to the rotation axis of the Earth, and y completes the right-handed orthogonal set (Y = Z * X). Geocentric Inertial (GCI) and Earth-Centered Inertial (ECI) are the same as GEI.

## J2000: Geocentric Equatorial Inertial for epoch J2000.0 (GEI2000)

Also known as Mean Equator and Mean Equinox of J2000.0 (Julian date 2451545.0 TT (Terrestrial Time), or 2000 January 1 noon TT, or 2000 January 1 11:59:27.816 TAI or 2000 January 1 11:58:55.816 UTC.) This system has X-axis aligned with the mean equinox for epoch J2000; Z-axis is parallel to the rotation axis of the Earth, and Y completes the right-handed orthogonal set.

# [rbsp_general012.tf](https://drive.google.com/file/d/1lArjp_YSxwHPp1g1mmqgjYRHYhgAx2eK/view?usp=drive_link)

## GEI

GEI is therefore defined to be an alias for SPICE J2000, where this is implemented by using the identity matrix.

## GEI_TOD

A true of date version of GEI, this is basically an instantaneous GEI for a given epoch, meaning that both precession and nutation of the equinox (discussed above) are accounted for.

```
PREC_MODEL = 'EARTH_IAU_1976'
NUT_MODEL  = 'EARTH_IAU_1980'
```

## GEI_MOD

Cites [NAIF Toolkit](https://drive.google.com/file/d/1rFr8r24P11MU95f9fDiZf2frKPBhKv7r/view?usp=drive_link)

> "Mean Ecliptic and Equinox of Date Frames are closely related to mean equator and equinox of date frames: for a given body, the former is obtained by rotating the latter about the X-axis by the mean obliquity of date.

> The term "mean equator" indicates that orientation of a body's equatorial plane is modeled accounting for precession. The "mean equinox" is the intersection of the body's mean orbital plane with the mean equatorial plane. The X-axis of such a frame is aligned with the cross product of the north-pointing vectors normal to the body's mean equator and mean orbital plane of date. The Z-axis is aligned with the second of these normal vectors. The Y axis is the cross product of the Z and X axes. The term ``of date'' means that these axes are evaluated at a specified epoch. "

> The Z axis of this frame is the pole of the mean ecliptic, and is used to define GSE.

```
PREC_MODEL = 'EARTH_IAU_1976'
```

## MEAN_ECLIP

```
PREC_MODEL  = 'EARTH_IAU_1976'
OBLIQ_MODEL = 'EARTH_IAU_1980'
```

# [Hapgood 1995](https://drive.google.com/file/d/1JFZApinOVlJpzgEQ0qhLpP5XUfOjjl9v/view?usp=drive_link)

When the inertial coordinate system is expressed in an epoch-of-date form there is, by convention, the option to ignore nutation effects. If the coordinate system is based on the average position of the rotation axis and the plane of the ecliptic allowing only for precession, it is known as the mean epoch-of-date system. If, however, it is based on their actual position allowing for precession and nutation, it is known as the true epoch-of-date system. We have already shown that the effect of nutation may be ignored in space physics coordinate transformations. Thus we may also neglect the difference between the mean and true epochs-of-date. We need only consider the difference between the epoch-of-date and standard epochs such as J2000.0.

# [Franz and Harper](https://drive.google.com/file/d/1x0T2L57-SqXaDsq2nZEYU5RmWsSLGuNC/view?usp=drive_link)

## GEI_J2000

* XY-plane Earth mean equator at J2000.0
* X-axis First point of Aries, i.e. vector(Earth-Sun) of vernal equinox of date

## GEI_D (Mean Geocentric Earth Equatorial) (Hapgood 1995)

* XY-plane Earth mean equator of date
* X-axis First point of Aries, i.e. vector(Earth-Sun) of vernal equinox of date

## GEI_T (True Geocentric Earth Equatorial) (Hapgood 1995)

Base system for actual position of objects

* XY-plane Earth true equator of date
* X-axis First point of Aries, i.e. vector(Earth-Sun) of vernal equinox of date
