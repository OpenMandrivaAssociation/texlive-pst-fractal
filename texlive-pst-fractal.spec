# revision 16958
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-fractal
# catalog-date 2010-02-10 21:21:32 +0100
# catalog-license lppl
# catalog-version 0.06
Name:		texlive-pst-fractal
Version:	0.06
Release:	1
Summary:	Draw fractal sets using PSTricks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-fractal
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-fractal.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-fractal.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package will draw the Julia and Mandelbrot sets, the
Sierpinski triangle, Koch flake, and Apollonius Circle as well
as fractal trees (which need not be balanced) with a variety of
different parameters (including varying numbers of iterations).
The package uses the pst-xkey package, part of the xkeyval
distribution.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
