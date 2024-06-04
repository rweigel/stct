The following are notes on the Centered Dipole coordinate frame.

This coordinate frame has been referred to as MAG, CD, GM, and "geomagnetic".

# [Hapgood 1995](https://drive.google.com/file/d/1JFZApinOVlJpzgEQ0qhLpP5XUfOjjl9v/view?usp=drive_link)

* $Y = $ Intersection between geographic equator and the geographic meridian $90^{\circ}$ East of the meridian containing the dipole axis
* $Z = $ Dipole axis

# [Franz and Harper](https://drive.google.com/file/d/1x0T2L57-SqXaDsq2nZEYU5RmWsSLGuNC/view?usp=drive_link)

* +Z-axis: Northern Earth dipole axis of date
* +Y-axis: cross-product of Geographic North Pole of date and +Z-axis.

# [SSCWeb](https://sscweb.gsfc.nasa.gov/users_guide/Appendix_C.shtml)

GM: Geomagnetic coordinate system. Z-axis points to the Geomagnetic north pole (in Greenland). The positive X-axis points towards the great circle encompassing the North and South Geomagetic poles and lies in the geomagnetic equatorial plane in the segment that is in the western hemisphere. (The South GM pole is the antipode of the North GM pole.) Earth-centered Dipole is invoked. Y completes the triad.

# [Russell 1971](https://drive.google.com/file/d/1zAAVba4I8JU2tpfhXeN1Y-rX5ogQTN3D/view)

The geomagnetic coordinate system (MAG) is defined so that its Z-axis is parallel to the magnetic dipole axis ... The Y-axis of this system is perpendicular to the geographic poles such that if $D$ is the dipole position and $S$ is the south pole, $Y=D\times S$. Finally, the $X$-axis completes a right-handed orthogonal set.

# [Laundal and Richmond 2017](https://drive.google.com/file/d/1JO-43r4Z3E6gTBG1-B2Wo_npMwQwoTc_/view)

Centered dipole coordinates are defined so that the Cartesian $z$ axis aligns with the dipole axis, pointing towards the centered dipole pole in the NH (i.e. the direction of $\hat{\mathbf{m}}$$^1$). The $y$ axis is perpendicular to the plane containing the dipole axis and the rotation axis of the Earth ($\hat{\mathbf{z}}\_\text{GEO}$). The $x$ axis completes a right-handed system. Mathematically, the base vectors are $\hat{\mathbf{m}}$

$^I$ defined earlier as a unit vector pointing antiparallel to a centered dipole approximation of Earth's field.

$\hat{\mathbf{z}}\_\text{cd} = \hat{\mathbf{m}}\_\text{geo}$ (subscript $\text{geo}$ not in equation, but implied by earlier definition).

$\hat{\mathbf{y}}\_\text{cd} = \hat{\mathbf{z}}\_\text{geo} \times \hat{\mathbf{z}}\_\text{cd}/|\hat{\mathbf{z}}\_\text{geo} \times \hat{\mathbf{z}}\_\text{cd}|$$^{II}$

$^{II}$ why is the denominator needed?

$\hat{\mathbf{x}}\_\text{CD} = \hat{\mathbf{y}}\_\text{CD} \times \hat{\mathbf{z}}\_\text{CD}$

# Reproducibility

For reproducibility, the three constants, or an algorithm for computing them, in $\mathbf{m}\_\text{GEO}$ must be given. Some implementations of the CD coordinate frame use only values listed in IGRF tables, which apply to a 5-year time window (and may change unless the values are definitive). Other implementations use constants that are based on interpolation, so, for example, the $\hat{\mathbf{z}}\_\text{CD}$ direction at a time within a IGRF 5-year time window depends on the values in the prior and following IGRF time window.