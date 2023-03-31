%bcond_with check
%global debug_package %{nil}

%global crate sysctl

Name:           rust-%{crate}
Version:        0.4.3
Release:        2
Summary:        Simplified interface to libc::sysctl

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/sysctl
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging
%if ! %{__cargo_skip_build}
BuildRequires:  (crate(bitflags/default) >= 1.0.0 with crate(bitflags/default) < 2.0.0)
BuildRequires:  (crate(byteorder/default) >= 1.0.0 with crate(byteorder/default) < 2.0.0)
BuildRequires:  (crate(libc/default) >= 0.2.34 with crate(libc/default) < 0.3.0)
BuildRequires:  (crate(thiserror/default) >= 1.0.2 with crate(thiserror/default) < 2.0.0)
BuildRequires:  (crate(walkdir/default) >= 2.2.8 with crate(walkdir/default) < 3.0.0)
%endif

%global _description %{expand:
Simplified interface to libc::sysctl.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(sysctl) = 0.4.3
Requires:       cargo
Requires:       (crate(bitflags/default) >= 1.0.0 with crate(bitflags/default) < 2.0.0)
Requires:       (crate(byteorder/default) >= 1.0.0 with crate(byteorder/default) < 2.0.0)
Requires:       (crate(libc/default) >= 0.2.34 with crate(libc/default) < 0.3.0)
Requires:       (crate(thiserror/default) >= 1.0.2 with crate(thiserror/default) < 2.0.0)
Requires:       (crate(walkdir/default) >= 2.2.8 with crate(walkdir/default) < 3.0.0)

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT
%doc README.md CHANGELOG.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(sysctl/default) = 0.4.3
Requires:       cargo
Requires:       crate(sysctl) = 0.4.3

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif
