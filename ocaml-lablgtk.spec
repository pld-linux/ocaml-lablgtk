Summary:	GTK+ binding for OCaml
Summary(pl):	Wi±zania GTK+ dla OCamla
Name:		ocaml-lablgtk
Version:	1.2.3
Release:	1
License:	LGPL
Group:		Libraries
URL:		http://wwwfun.kurims.kyoto-u.ac.jp/soft/olabl/lablgtk.html
Source0:	http://wwwfun.kurims.kyoto-u.ac.jp/soft/olabl/dist/lablgtk-%{version}.tar.gz
BuildRequires:	gtk+-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	libglade-devel
BuildRequires:	libxml-devel
BuildRequires:	ocaml-camlp4 >= 3.04-7
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GTK+ binding for OCaml. GNOME and Glade support is included. This
package contains files needed to run bytecode OCaml programs using
LablGtk.

%description -l pl
Wi±zania GTK+ dla OCamla. Wsparcie dla GNOME i Glade jest do³±czone.
Pakiet ten zawiera binaria potrzebne do uruchamiania programów
u¿ywaj±cych LablGtk.

%package devel
Summary:	GTK+ binding for OCaml - development part
Summary(pl):	Wi±zania GTK+ dla OCamla - cze¶æ programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml

%description devel
GTK+ binding for OCaml. GNOME and Glade support is included. This
package contains files needed to develop OCaml programs using LablTk.

%description devel -l pl
Wi±zania GTK+ dla OCamla. Wsparcie dla GNOME i Glade jest do³±czone.
Pakiet ten zawiera pliki niezbêdne do tworzenia programów u¿ywaj±cych
LablTk.

%package toplevel
Summary:	GTK+ binding for OCaml - interactive system
Summary(pl):	Wi±zania GTK+ dla OCamla - system interaktywny
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
%requires_eq	ocaml

%description toplevel
GTK+ binding for OCaml. GNOME and Glade support is included. This
package contains OCaml toplevel interactive system linked with
lablgtk.

%description toplevel -l pl
Wi±zania GTK+ dla OCamla. Wsparcie dla GNOME i Glade jest do³±czone.
Pakiet ten zawiera system interaktywny OCamla zlinkowany z lablgtk.

%prep
%setup -q -n lablgtk-%{version}

%build
%{__make} \
	configure \
	CC="%{__cc} %{rpmcflags} -fpic" \
	USE_CC=1 \
	USE_GNOME=1 \
	USE_GLADE=1
%{__make} all opt

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	INSTALLDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml/lablgtk \
	LIBDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml \
	BINDIR=$RPM_BUILD_ROOT%{_bindir}

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -r examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# .mli files stay, they are the only documentation, but .ml go
rm -f $RPM_BUILD_ROOT%{_libdir}/ocaml/lablgtk/*.ml
gzip -9nf $RPM_BUILD_ROOT%{_libdir}/ocaml/lablgtk/*.mli
mv $RPM_BUILD_ROOT%{_libdir}/ocaml/lablgtk/*.gz .

(cd $RPM_BUILD_ROOT%{_libdir}/ocaml/ && ln -s lablgtk/dll*.so .)

# make META for findlib
install -d $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/lablgtk
cat > $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/lablgtk/META <<EOF
# Specifications for the "lablgtk" library:
requires = ""
version = "%{version}"
directory = "+lablgtk"
archive(byte) = "lablgtk.cma gtkInit.cmo"
archive(native) = "lablgtk.cmxa gtkInit.cmx"
archive(byte,gnome) = "lablgnome.cma"
archive(native,gnome) = "lablgnome.cmxa"
archive(byte,glade) = "lablglade.cma"
archive(native,glade) = "lablglade.cmxa"
linkopts = ""
EOF

gzip -9nf README CHANGES COPYING

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/ocaml/lablgtk
%attr(755,root,root) %{_libdir}/ocaml/lablgtk/dll*.so
%{_libdir}/ocaml/dll*.so

%files devel
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/lablgladecc
%{_libdir}/ocaml/lablgtk/*.cm*
%{_libdir}/ocaml/lablgtk/*.[hao]
%attr(755,root,root) %{_libdir}/ocaml/lablgtk/varcc
%{_examplesdir}/%{name}-%{version}
%{_libdir}/ocaml/site-lib/lablgtk

%files toplevel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lablgtk
%attr(755,root,root) %{_libdir}/ocaml/lablgtk/lablgtktop
%attr(755,root,root) %{_libdir}/ocaml/lablgtk/lablgtktop_t
