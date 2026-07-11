%global tl_name pst-fractal
%global tl_revision 79409

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.13
Release:	%{tl_revision}.1
Summary:	Draw fractal sets using PSTricks
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-fractal
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-fractal.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-fractal.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package uses PSTricks to draw the Julia and Mandelbrot sets, the
Sierpinski triangle, Koch flake, and Apollonius Circle as well as
fractal trees (which need not be balanced) with a variety of different
parameters (including varying numbers of iterations). The package uses
the pst-xkey package, part of the xkeyval distribution.

