CD (Centered Dipole) - $\hat{\mathbf{z}}\_\text{CD}$ is anti-parallel to the unit vector, $\hat{\mathbf{m}}\_\text{GEO}$, that is in the direction Earth's magnetic moment vector, $\mathbf{m}\_\text{GEO}$, where $\mathbf{m}\_\text{GEO}$ is from a dipole approximation of Earth's internal magnetic field. This coordinate frame has been referred to as MAG, CD, and "geomagnetic".

$\hat{\mathbf{y}}\_\text{CD} = \hat{\mathbf{z}}\_\text{GEO} \times \hat{\mathbf{z}}\_\text{CD}$

$\hat{\mathbf{x}}\_\text{CD} = \hat{\mathbf{y}}\_\text{CD} \times \hat{\mathbf{z}}\_\text{CD}$

For reproducibility, the three constants, or an algorithm for computing them, in $\mathbf{m}\_\text{GEO}$ must be given. Some implementations of the CD coordinate frame use only values listed in IGRF tables, which apply to a 5-year time window (and may change unless the values are definitive). Other implementations use constants that are based on interpolation, so, for example, the $\hat{\mathbf{z}}\_\text{CD}$ direction at a time within a IGRF 5-year time window depends on the values in the prior and following IGRF time window.