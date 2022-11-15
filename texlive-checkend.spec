Name:		texlive-checkend
Version:	51475
Release:	1
Summary:	Extend "improperly closed environment" messages
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/checkend
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/checkend.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/checkend.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
When an environment is left open, LaTeX gives an error at the
end of the document. However it only informs about the first of
them, while the rest are shown with meaningless errors: (\end
occurred inside a group at level N) This package replaces these
errors with more useful messages which show which environments
(in reverse order) were not closed. There are no user macros:
just use the package.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/checkend
%doc %{_texmfdistdir}/doc/latex/checkend

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
