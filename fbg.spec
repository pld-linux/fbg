Summary:	Falling Blocks Game
Summary(pl):	Falling Blocks Game - gra w spadaj±ce klocki
Name:		fbg
Version:	0.9
Release:	1
License:	GPLv2
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/fbg/%{name}-%{version}.tar.gz
Patch0:		%{name}-libgl.patch
Patch1:		%{name}-FHS.patch
URL:		http://derajdezine.vze.com/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libmikmod-devel
BuildRequires:	libstdc++-devel
BuildRequires:	physfs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Falling Blocks Game.

%description -l pl
Falling Blocks Game - gra w spadaj±ce klocki.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/fbg
%{_mandir}/man6/*
