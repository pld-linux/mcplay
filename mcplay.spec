Summary:	A text terminal music player
Summary(pl):	Terminalowy odtwarzacz muzyczny
Name:		mcplay
Version:	0.3i
Release:	2
License:	GPL
Group:		Applications/Sound
Source0:	http://www.yahuxo.de/mcplay/%{name}-%{version}.tar.gz
# Source0-md5:	11448f55ea7d6b337ec3b9e2c0bf7b13
Patch0:		%{name}-config.patch
URL:		http://www.yahuxo.de/mcplay/
BuildRequires:	lirc-devel
BuildRequires:	ncurses-devel
Requires:	mpg123
Requires:	playmidi
Requires:	sox
Requires:	vorbis-tools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A text terminal MP3 player. It can play MP3, ogg, WAV, mid and other
types of music files.

%description -l pl
Terminalowy odtwarzacz MP3. Mo¿e odtwarzaæ pliki muzyczne MP3, ogg,
WAV, mid i inne.

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
