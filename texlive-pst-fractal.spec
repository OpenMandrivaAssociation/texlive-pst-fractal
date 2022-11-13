Name:		texlive-pst-fractal
Version:	64714
Release:	1
Summary:	Draw fractal sets using PSTricks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-fractal
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-fractal.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-fractal.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package will draw the Julia and Mandelbrot sets, the
Sierpinski triangle, Koch flake, and Apollonius Circle as well
as fractal trees (which need not be balanced) with a variety of
different parameters (including varying numbers of iterations).
The package uses the pst-xkey package, part of the xkeyval
distribution.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/pst-fractal/pst-fractal.pro
%{_texmfdistdir}/tex/generic/pst-fractal/pst-fractal.tex
%{_texmfdistdir}/tex/latex/pst-fractal/pst-fractal.sty
%doc %{_texmfdistdir}/doc/generic/pst-fractal/Changes
%doc %{_texmfdistdir}/doc/generic/pst-fractal/README
%doc %{_texmfdistdir}/doc/generic/pst-fractal/pst-fractal-doc.bib
%doc %{_texmfdistdir}/doc/generic/pst-fractal/pst-fractal-doc.pdf
%doc %{_texmfdistdir}/doc/generic/pst-fractal/pst-fractal-doc.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc %{buildroot}%{_texmfdistdir}
