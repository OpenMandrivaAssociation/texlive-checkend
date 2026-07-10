%global tl_name checkend
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Extend improperly closed environment messages
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/checkend
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/checkend.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/checkend.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
When an environment is left open, LaTeX gives an error at the end of the
document. However it only informs about the first of them, while the
rest are shown with meaningless errors: (\end occurred inside a group at
level N) This package replaces these errors with more useful messages
which show which environments (in reverse order) were not closed. There
are no user macros: just use the package.

