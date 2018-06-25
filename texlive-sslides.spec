# revision 32293
# category Package
# catalog-ctan /macros/latex/contrib/sslides
# catalog-date 2013-12-01 17:33:13 +0100
# catalog-license lppl1.3
# catalog-version undef
Name:		texlive-sslides
Version:	20180303
Release:	1
Summary:	Slides with headers and footers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/sslides
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sslides.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sslides.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The class provides a variant of the LaTeX standard slides
class, in which the user may add headers and footers to the
slide.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/sslides/sslides.cls
%doc %{_texmfdistdir}/doc/latex/sslides/land-sample-slide.pdf
%doc %{_texmfdistdir}/doc/latex/sslides/land-sample-slide.tex
%doc %{_texmfdistdir}/doc/latex/sslides/port-sample-slide.pdf
%doc %{_texmfdistdir}/doc/latex/sslides/port-sample-slide.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
