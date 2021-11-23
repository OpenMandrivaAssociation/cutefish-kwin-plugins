%define oname kwin-plugins

Name:           cutefish-kwin-plugins
Version:        0.5
Release:        1
Summary:        Some configurations and plugins of KWin.
License:        GPL-3.0-or-later
Group:          System/GUI/Other
URL:            https://github.com/cutefishos/kwin-plugins
Source:         https://github.com/cutefishos/kwin-plugins/archive/refs/tags/%{version}/%{oname}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  cmake(KDecoration2)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KWinEffects)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KWinDBusInterface)
BuildRequires:  cmake(KF5Wayland)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5UiTools)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(xcb-atom)

%description
Cutefish Desktop KWin Plugins.

%prep
%autosetup -n %{oname}-%{version} -p1

%build
%cmake
%make_build

%install
%make_install -C build

%files
%license LICENSE
%doc README.md
%config(noreplace) %{_sysconfdir}/xdg/kglobalshortcutsrc
%config(noreplace) %{_sysconfdir}/xdg/kwinrc
%config(noreplace) %{_sysconfdir}/xdg/kwinrulesrc
%dir %{_datadir}/kwin
%dir %{_datadir}/kwin/effects
%{_datadir}/kwin/effects/cutefish_popups/
%{_datadir}/kwin/effects/cutefish_squash/
%{_datadir}/kwin/effects/cutefish_scale/
%dir %{_datadir}/kwin/scripts
%{_datadir}/kwin/scripts/cutefishlauncher/
%dir %{_datadir}/kwin/tabbox
%{_datadir}/kwin/tabbox/cutefish_thumbnail/
#dir #{_libqt5_plugindir}/kwin
#dir #{_libqt5_plugindir}/kwin/effects
#dir #{_libqt5_plugindir}/kwin/effects/plugins
#{_libqt5_plugindir}/kwin/effects/plugins/libroundedwindow.so
#dir #{_libqt5_plugindir}/org.kde.kdecoration2
#{_libqt5_plugindir}/org.kde.kdecoration2/libcutefishdecoration.so
