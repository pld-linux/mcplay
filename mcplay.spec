Summary:	A console music player
Summary(pl):	Konsolowy odtwarzacz muzyczny
Name:		mcplay
Version:	0.3i
Release:	1
License:	GPL
Group:		Applications/Sound
Source0:	http://www.yahuxo.de/mcplay/%{name}-%{version}.tar.gz
Patch0:		%{name}-config.patch
URL:		http://www.yahuxo.de/mcplay/
BuildRequires:	glib-devel
BuildRequires:	lirc-devel
BuildRequires:	ncurses-devel
Requires:	mpg123
Requires:	playmidi
Requires:	sox
Requires:	vorbis-tools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A console mp3 player. It can play mp3, ogg, wav, mid and other types
of music files.

%description -l pl
Konsolowy odtwarzacz mp3. Mo¿e odtwarzaæ pliki muzyczne mp3, ogg, wav,
mid i inne.

%prep
%setup -q
%patch -p1

%build
%{__make} MY_CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install mcplay $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
