Name:		texlive-sslides
Version:	32293
Release:	2
Summary:	Slides with headers and footers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/sslides
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sslides.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sslides.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
