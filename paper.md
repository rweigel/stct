Moved to Overleaf
# Title

Coordinate Frames and Transforms in Space Physics: Terms, Definitions, and Implementations

# Authors?

R.S. Weigel, A.Y. Shih, R. Ringuette, I. Christopher, S.M. Petrinec, S. Turner, R.M. Candey, and B. Cecconi

# Abstract

In space physics, terms for coordinate systems (e.g., GSE, GSM) are used interchangeably when slight differences exist in the definition or implementation details used to compute a vector in a coordinate systems. In this work, we provide (1) a set of terms for coordinate systems derived from frequently cited papers, online resources, and software packages, (2) definitions in a common style, and (3) details on implementation choices that may affect the result. We also compare results from frequently cited online resources and software packages to enable estimates of uncertainty based on implementation choices. The general result is that the angular differences in transforms between two different coordinate systems using $x$ different software packages is ~$Y$.

# Introduction

The motivation for this work is that a standard to reference should be available for when we write, "Measurements are in coordinate system XYZ." In space physics, the definition of a coordinate system is typically provided via a reference that describes it. However, not all commonly cited references contain the same coordinate system definitions, use the same acronyms, or provide equivalent definitions. (In this work, we use the convention term "coordinate system" consistent with common usage but note that coordinate "coordinate frame" is the technically correct term.)

A second motivation is that the uncertainty associated with how a coordinate system transform is implemented in software has not been discussed in the literature, presumably because other uncertainties, such as measurement uncertainty, are expected to be much larger. However, we show that there can be situations where differences in implementation give significant differences. Also, if one implements a new transform library, it is natural to compare it with other implementations. If there are differences, a natural question is if differences are due to an implementation error or a difference in the choice of how the transform was implemented.

The terms for coordinate systems used in this work are based on a review of frequently cited papers and software and other resources or standards, which includes [Russell 1971](https://drive.google.com/file/d/1zAAVba4I8JU2tpfhXeN1Y-rX5ogQTN3D/view), [Kivelson and Russell](https://drive.google.com/file/d/1-4151VP-y5GVOzcRMThbx0ZKc-o1hCQ2/view), [Franz and Harper 2017](https://drive.google.com/file/d/1x0T2L57-SqXaDsq2nZEYU5RmWsSLGuNC/view); see also [Franz and Harper 2002](https://drive.google.com/file/d/1-GvR6sbPC-pkAbPRp1_WIaU6f2QaEUvL/view) and [supplementary material](https://www2.mps.mpg.de/homes/fraenz/systems/), [Hapgood 1992](https://drive.google.com/file/d/1JFZApinOVlJpzgEQ0qhLpP5XUfOjjl9v/view); see also [Hapgood 1995](https://drive.google.com/file/d/1lof3qGSi90VRD_htvg8eEVZdfXpN64_w/view) and [Hapgood 1997](https://drive.google.com/file/d/1fYQuh0z3xb7o8zRi-AYr80k8GcLNilIA/view), [Laundal and Richmond 2016](https://drive.google.com/file/d/1JO-43r4Z3E6gTBG1-B2Wo_npMwQwoTc_/view), [SpacePy](https://spacepy.github.io/coordinates.html#magnetospheric-systems), [SunPy](https://docs.astropy.org/en/stable/coordinates/ref_api.html#module-astropy.coordinates), [SSCWeb](https://sscweb.gsfc.nasa.gov/users_guide/Appendix_C.shtml), and [SPASE](https://spase-group.org/data/model/spase-2.4.0/spase-2_4_0_xsd.html#CoordinateSystemName).


# Terminology

* Coordinate frame: an origin and three mutually orthogonal axes;
* Coordinate system: a way of representing a position in a coordinate frame, for example, spherical or cylindrical.
* True of Date (nutation accounted for)
* Mean of Date (nutation excluded or averaged over; from rbsp SPICE kernel, which cites Franz and Harper 2002: 'Mean-of-date' refers to a frame or coordinate system where only precession is used. The term 'True-of-date' adds on the nutation and is the actual best representation for the first point of Aries at a given epoch.
* obliquity (tilt of the Earth's rotation axis with respect to the ecliptic plane),
* precession (rotation of Earth's rotation axis around the ecliptic pole),
* nutation (perturbations to precession path),
* polar motion (IERS table; in SunPy, [Geocentric Earth Equatorial](https://docs.sunpy.org/en/stable/generated/api/sunpy.coordinates.GeocentricEarthEquatorial.html) (what is "abberation due to Earth motion"?) does not include true polar motion GEO does; 10-20 meters), and
* planetary precession (motion of the ecliptic with respect to the fixed stars).

* Earth's Equatorial plane
* Ecliptic Plane (plane of Earth's orbit; see Hapgood 1995 for a discussion of how this changes.)
* Epoch is used to mean a reference date and time (an instant, rather than a period of time as is another common usage of "epoch")
* Aries - the Aries constellation
* First point of Aries, i.e. vector(Earth-Sun) at the time of the vernal equinox
* Vernal Equinox (a point in the sky) vs Vernal Equinox (a time)
* Hapgood uses "epoch of date"; Franz and Harper use "true of date"


# Coordinate Systems

Ideally, the definitions given here allow reproducibility of transforms at the level of machine precision. Although we have provided extra terms to describe similar coordinate frames (e.g., three variations on `GEI`), additional details about the implementation of the transform are needed to allow for exact reproducibility. Given the number of possible implementation choices for each coordinate frame, this standard should be regarded as only partially achieving this goal.

For example, the MAG frame depends on the location of the $Z$-axis of the centered dipole approximation of Earth's main field. Software libraries typically use coefficients from the IGRF model to determine the location of the $Z$-axis. However, some implementations use interpolation of the IGRF coefficients, which apply to a 5-year time span [Alken et al., 2021](https://earth-planets-space.springeropen.com/articles/10.1186/s40623-020-01288-x). In addition, the [IGRF coefficients may change](https://www.ngdc.noaa.gov/IAGA/vmod/igrf_old_models.html), so for reproducibility, the version of the IGRF model must be specified. Instead of enumerating all of the possible combinations of (interpolation/no interpolation, IGRF model) permutations, we provide only two options: `MAG`, `MAG_S`, `MAG_US` (to indicate that one or more of smoothing, extrapolation, interpolation was used). Need to find best term.

All of the definitions given in this section use the same description style. This deviates from the literature, where some frames are described using this style and others using a style that involves describing rotations.

## `GEI`

**Term**: `GEI`

**Label**: Geocentric Equatorial Inertial

**Definition**:

* +Z: `GEO Z`
* +X: intersection of Earth's equatorial plane and the ecliptic plane, with positive in the direction of Aries
* +Y: `GEI Z` x `GEI X`

**Discussion**

Will need to address the fact that primary axes can be swapped.

There are two basic categories of the Geocentric Equatorial Inertial (GEI) coordinate frame in common use.

%$^I$ Other variations include "Geocentric Earth Equatorial" (Franz and Harper 2017) and "Geocentric Celestial Inertial" (GCI) (Russell 1971). Note that Franz and Harper 2017 use "Geocentric Earth Equatorial" and cite Hapgood 1995 in the first bullet of section 3.1. However, Hapgood 1995 only uses "Geocentric Equatorial Inertial" and an explanation is not given for the change in name.

1. An inertial coordinate frame in which the axes are fixed relative to the distant stars. The definition depends on the epoch at which the axes are determined, the catalog used for the positions of the distant starts and the 

There are several versions that depend on how and which time-varying effects are accounted for but evaluate them at a specific date and time (epoch).

1. A non-inertial coordinate frame. There are several versions, depending on which how and which of the following time-varying effects are were accounted for
   * obliquity (tilt of the Earth's rotation axis with respect to the ecliptic plane),
   * precession (rotation of Earth's rotation axis around the ecliptic pole),
   * nutation (perturbations to precession path),
   * polar motion (IERS table; in SunPy, [Geocentric Earth Equatorial](https://docs.sunpy.org/en/stable/generated/api/sunpy.coordinates.GeocentricEarthEquatorial.html) (what is "abberation due to Earth motion"?) does not include true polar motion GEO does; 10-20 meters), and
   * planetary precession (motion of the ecliptic with respect to the fixed stars).


Note that Franz and Harper 2017 define `GEI` as "Geocentric Earth Equatorial", perhaps to account for the fact that not all `GEI` definitions are actually inertial. Here we use the label "Geocentric Equatorial Inertial" for historical reasons. SunPy uses the term [`GeocentricEarthEquatorial`](https://docs.sunpy.org/en/stable/generated/api/sunpy.coordinates.frames.GeocentricEarthEquatorial.html) with definition "A coordinate or frame in the Geocentric Earth Equatorial (GEI) system".

## `GEI_TOD`

**Term**: `GEI_TOD`

**Label**: Geocentric Equatorial Inertial True-of-Date

**Definition**:

`GEI` where `GEI Z` is based on True-of-Date values and `GEI X` is the True-of-Date intersection of Earth's equatorial plane and the ecliptic plane and thus the X-axis lies in both planes, with positive in the direction of the Aries.

**AKA**
* `GEI_T` [Franz and Harper 2002](https://drive.google.com/file/d/1-GvR6sbPC-pkAbPRp1_WIaU6f2QaEUvL/view)
* `ECITOD` [SpacePy](https://github.com/spacepy/spacepy/blob/main/spacepy/coordinates.py#L41C1-L42C49)

## `GEI_MOD`

**Term**: `GEI_MOD`

**Label**: Geocentric Equatorial Inertial Mean-of-Date

**Definition**:

`GEI_TOD` except `GEI X` and `GEI Z` are based on Mean-of-Date values

**AKA**
* Geocentric Earth Equatorial ([AstroPy](https://docs.sunpy.org/en/stable/generated/api/sunpy.coordinates.GeocentricEarthEquatorial.html))
* `GEI_D` ([Franz and Harper 2002](https://drive.google.com/file/d/1-GvR6sbPC-pkAbPRp1_WIaU6f2QaEUvL/view))
* `ECIMOD` ([SpacePy](https://github.com/spacepy/spacepy/blob/main/spacepy/coordinates.py#L41C1-L42C49))

## `GEI_J2000`

**Term**: `GEI_J2000`

**Label**: Geocentric Equatorial Inertial J2000

**Definition**:

* +Z: `GEO Z`
* +X: intersection of Earth's equatorial plane and the ecliptic plane, with positive in the direction of Aries and at time J2000.0
* +Y: `GEI Z` x `GEI X`

**AKA**
* `J2000` ([SSCWeb](https://sscweb.gsfc.nasa.gov/users_guide/Appendix_C.shtml))
* `GEI_J2000` ([Franz and Harper 2002](https://drive.google.com/file/d/1-GvR6sbPC-pkAbPRp1_WIaU6f2QaEUvL/view))
* `ECIJ2000` ([SpacePy](https://github.com/spacepy/spacepy/blob/main/spacepy/coordinates.py#L41C1-L42C49))
* `EME2000` (in tracers docs?)

## `GEO`

**Term**: `GEO`

**Label**: Geographic

**Definition**:

* +Z: geographic north pole
* +X: intersection of Greenwich meridian and geographic equator
* +Y: `GEO Z` x `GEO X`

**Related**
* `GEO_TOD`

## `GEO_TOD`

**Term**: `GEO_TOD`

**Label**: Geographic True of Date

**Definition**:

`GEO` when `GEO Z` and `GEO X` are computed using true-of-date values

**Related**
* `GEO`

## `GSM`
**Term**: `GSM`

**Label**: Geocentric Solar Magnetospheric

**Definition**:

* +X: `GEI X`
* +Y: `GSM X` x `CD Z`
* +Z: `GSM X` x `GSM Y`

**AKA**
* Geocentric Solar Magnetic (GSM) (Laundal and Richmond, 2017)
* Solar Magnetospheric (SM) (see Table I in Russell 1971)

**Related**
* `GSM_TOD`

## `GSM_TOD`

**Term**: `GSM_TOD`

**Label**: Geocentric Solar Magnetic True of Date

**Definition**:

`GSM` when `GSM X` and `MAG Z` are computed using True-of-Date values

## `GDZ`

**Term**: `GDZ`

**Label**: Geodetic

**Definition**:

**Used by**

* SpacePy

## `DM`

## `ECD`

## `ECEF`

## `CGM`

## `CD`


## `MAG`

**Term**: `MAG`

**Label**: Geomagnetic

**Definition**:

* +Z:  Opposite direction of dipole moment from centered dipole approximation of Earth's internal magnetic field in `GEO`
* +Y: `GEO Z` x `MAG Z`
* +X: `MAG Y` x `MAG Z`

**AKA**
* CD (Laundal and Richmond, 2017)
* GM (see Table I in Russell 1971)


## `SM`

**Term**: `SM`

**Label**: Solar Magnetic

**Definition**:

* +Z: `MAG Z`
* +Y: `MAG Z` x `GSM X`
* +X: `MAG Y` x `MAG Z`

## `GSEQ`

* +X: Vector from to center of Earth to the center of Sun
* +Y: `R_GEI` x `S_GEI`, where `R` is rotation axis of Sun in `GEI` and `S` is the position of the sun in `GEI`.

# Comparisons

## Spacecraft Ephemeris

Geotail GEI, GSE, and GSM; Max differences on the order of 1000 km (⅙ of an RE). Summarize results over long time span (say avg(|angle|)

Add a LEO s/c.

```
        X [km]        Y [km]         Z [km]   
CDAWeb: 144142.958    57271.425     -45363.263    2021-11-25T00:00:00.000Z (Using dataset GE_OR_DEF/GCI)
SSCWeb: 144237.089    58796.878     -44641.666    2021-11-25T00:00:00.000Z (Using dataset geotail/GEI/TOD)
SSCWeb: 144427.979    58090.032     -44948.816    2021-11-25T00:00:00.000Z (Using dataset geotail/GEI/J2K)

        X_GSE [km]    Y_GSE [km]    Z_GSE [km]   
CDAWeb: -96913.678    112140.816    -64398.839    2021-11-25T00:00:00.000Z (Using dataset GE_OR_DEF/GSE)
SSCWeb: -97844.503    111984.683    -64344.178    2021-11-25T00:00:00.000Z (Using dataset geotail/GSE)

        X_GSM [km]    Y_GSM [km]    Z_GSM [km]   
CDAWeb: -96913.678    110822.349    -66642.180    2021-11-25T00:00:00.000Z (Using dataset GE_OR_DEF/GSM)
SSCWeb: -97844.503    110030.273    -67631.954    2021-11-25T00:00:00.000Z (Using dataset geotail/GSM)
```

## Software Library Comparison

```
Time: [2015, 12, 30, 0, 0, 0]
                           x           y           z       magnitude
-----------------------------------------------------------------------------------
Input (GSE):           3.46410162  3.46410162  3.46410162  6.00000000
Output (GSM):                                                         ∠° wrt Input
-----------------------------------------------------------------------------------
cxform                 3.46410162  2.54340625  4.18701381  6.00000000 11.19612022
geopack_08_dp          3.46410162  2.54785114  4.18431052  6.00000000 11.14656002
pyspedas               3.46410162  2.54785080  4.18431073  6.00000000 11.14656386
spacepy                3.46410162  2.54710195  4.18476662  6.00000000 11.15491581
spacepy-irbem          3.46410162  2.54566083  4.18535391  5.99979803 11.16945855
spiceypy1              3.46410162  2.54651712  4.18512252  6.00000000 11.16143772
spiceypy2              3.46410162  2.54725501  4.18467345  6.00000000 11.15320876
sscweb                 3.46        2.55        4.18        5.99554001 11.10894044
sunpy                  3.46395412  2.54785162  4.18443234  6.00000000 11.14727882

max-min:               0.00410162  0.00659375  0.00701381  0.00445999  0.08717978
100*|max-min|/|max|:       0.1184%     0.2586%     0.1675%     0.0743%     0.7787%
If x, y, z are in R_E, then max-min angle corresponds to 58 km
```

