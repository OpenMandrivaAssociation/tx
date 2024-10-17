%define name	tx
%define version	1.2
%define release %mkrel 5

Name: 	 	%{name}
Summary: 	Graphical XML editor using QT4
Version: 	%{version}
Release: 	%{release}

Source:		tx_1-2_src.tar.bz2
URL:		https://www.gravitybind.com/
License:	GPL
Group:		Editors
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	imagemagick
BuildRequires:	qt4-devel

%description
Teddy is a tabular editor and display for XML files. It presents the structure
and content of XML files in a way that is both visually pleasing and easy to
use.

%prep
%setup -q -n %name

%build
/usr/lib/qt4/bin/qmake %name.pro
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
mkdir -p %buildroot/%_bindir
cp bin/tx %buildroot/%_bindir/%name

#menu
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{name}
Icon=%{name}
Name=TX
Comment=XML Editor
Categories=TextEditor;
EOF

#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
convert -size 48x48 images/tX.png $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
convert -size 32x32 images/tX.png $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
convert -size 16x16 images/tX.png $RPM_BUILD_ROOT/%_miconsdir/%name.png

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif
		
%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc CHANGES README
%{_bindir}/%name
%{_datadir}/applications/mandriva-%name.desktop
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png

