import streamlit as st
import json
import os

# ── Configuración de la página ──────────────────────────────────────────────
st.set_page_config(
    page_title="TecnoClass",
    page_icon="🏫",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── CSS personalizado ────────────────────────────────────────────────────────
st.markdown("""
<style>
    .main { background-color: #0f1117; }
    .stApp { background-color: #0f1117; }
    div[data-testid="stSidebar"] { background-color: #1a1a2e; }

    .tc-title {
        font-size: 2.2rem;
        font-weight: 800;
        color: #00e5a0;
        margin-bottom: 0.2rem;
    }
    .tc-subtitle {
        color: #8888aa;
        font-size: 0.95rem;
        margin-bottom: 1.5rem;
    }
    .tc-card {
        background: #16161f;
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 12px;
        padding: 1rem 1.2rem;
        margin-bottom: 0.75rem;
        color: #f0f0f5;
    }
    .tc-card strong { color: #00e5a0; }
    .tc-badge {
        display: inline-block;
        background: rgba(0,229,160,0.12);
        color: #00e5a0;
        border-radius: 100px;
        padding: 2px 10px;
        font-size: 0.8rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    .tc-empty {
        color: #555570;
        font-style: italic;
        padding: 1.5rem;
        text-align: center;
        background: #16161f;
        border-radius: 12px;
        border: 1px dashed rgba(255,255,255,0.08);
    }
    .success-msg {
        background: rgba(0,229,160,0.1);
        border: 1px solid rgba(0,229,160,0.3);
        border-radius: 8px;
        padding: 0.75rem 1rem;
        color: #00e5a0;
        font-weight: 600;
        margin: 0.5rem 0;
    }
    .stButton > button {
        background: #00e5a0 !important;
        color: #000 !important;
        font-weight: 700 !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.5rem 1.5rem !important;
        width: 100%;
    }
    .stButton > button:hover {
        background: #00ffb3 !important;
    }
    .stSelectbox label, .stTextInput label, .stNumberInput label {
        color: #8888aa !important;
        font-size: 0.85rem !important;
        font-weight: 500 !important;
    }
</style>
""", unsafe_allow_html=True)

# ── Persistencia de datos en session_state ───────────────────────────────────
GRADOS = ["SEXTO", "SEPTIMO", "OCTAVO", "NOVENO", "DECIMO", "UNDECIMO"]

def init_data():
    if "estudiantes" not in st.session_state:
        st.session_state.estudiantes = [
            {"Nombre": "Ana García",    "Edad": 12, "ID": "1001", "grado": "SEXTO"},
            {"Nombre": "Luis Martínez", "Edad": 13, "ID": "1002", "grado": "SEPTIMO"},
            {"Nombre": "María López",   "Edad": 14, "ID": "1003", "grado": "OCTAVO"},
            {"Nombre": "Carlos Ruiz",   "Edad": 15, "ID": "1004", "grado": "NOVENO"},
        ]
    if "profesores" not in st.session_state:
        st.session_state.profesores = [
            {"Nombre": "Prof. Ramírez", "Edad": 35, "ID": "2001", "Asignatura": "Matemáticas"},
            {"Nombre": "Prof. Torres",  "Edad": 42, "ID": "2002", "Asignatura": "Español"},
        ]

init_data()

# ── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown('<div class="tc-title">🏫 TecnoClass</div>', unsafe_allow_html=True)
    st.markdown('<div class="tc-subtitle">Sistema de Gestión Académica</div>', unsafe_allow_html=True)
    st.divider()

    menu = st.radio(
        "Navegación",
        [
            "🏠  Inicio",
            "👨‍🎓  Ver Estudiantes",
            "👩‍🏫  Ver Profesores",
            "➕  Matricular Estudiante",
            "➕  Registrar Profesor",
            "❌  Expulsar Estudiante",
            "❌  Despedir Profesor",
            "✏️  Actualizar Estudiante",
            "✏️  Actualizar Profesor",
        ],
        label_visibility="collapsed"
    )

    st.divider()
    total_est = len(st.session_state.estudiantes)
    total_prof = len(st.session_state.profesores)
    st.metric("Total Estudiantes", total_est)
    st.metric("Total Profesores", total_prof)

# ── Inicio ───────────────────────────────────────────────────────────────────
if menu == "🏠  Inicio":
    st.markdown('<div class="tc-title">Bienvenido a TecnoClass</div>', unsafe_allow_html=True)
    st.markdown('<div class="tc-subtitle">Sistema de gestión académica para instituciones educativas</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("👨‍🎓 Estudiantes", len(st.session_state.estudiantes))
    with col2:
        st.metric("👩‍🏫 Profesores", len(st.session_state.profesores))
    with col3:
        st.metric("📚 Grados activos", len(GRADOS))

    st.divider()
    st.markdown("### ¿Qué puedes hacer?")
    col1, col2 = st.columns(2)
    with col1:
        st.info("**Estudiantes** — Matricular, ver, actualizar y expulsar estudiantes por grado.")
    with col2:
        st.info("**Profesores** — Registrar, ver, actualizar y despedir profesores de la institución.")
    st.caption("💡 Usa el menú de la izquierda para navegar entre las funciones del sistema.")

# ── Ver Estudiantes ──────────────────────────────────────────────────────────
elif menu == "👨‍🎓  Ver Estudiantes":
    st.markdown('<div class="tc-title">Estudiantes Matriculados</div>', unsafe_allow_html=True)

    grado_sel = st.selectbox("Selecciona el grado", ["Todos"] + GRADOS)

    if grado_sel == "Todos":
        lista = st.session_state.estudiantes
    else:
        lista = [e for e in st.session_state.estudiantes if e["grado"] == grado_sel]

    if lista:
        for e in lista:
            st.markdown(f"""
            <div class="tc-card">
                <span class="tc-badge">{e['grado']}</span><br>
                <strong>Nombre:</strong> {e['Nombre']} &nbsp;|&nbsp;
                <strong>Edad:</strong> {e['Edad']} &nbsp;|&nbsp;
                <strong>ID:</strong> {e['ID']}
            </div>
            """, unsafe_allow_html=True)
        st.caption(f"Total: {len(lista)} estudiante(s)")
    else:
        st.markdown('<div class="tc-empty">No hay estudiantes en este grado.</div>', unsafe_allow_html=True)

# ── Ver Profesores ───────────────────────────────────────────────────────────
elif menu == "👩‍🏫  Ver Profesores":
    st.markdown('<div class="tc-title">Profesores Registrados</div>', unsafe_allow_html=True)

    if st.session_state.profesores:
        for p in st.session_state.profesores:
            st.markdown(f"""
            <div class="tc-card">
                <span class="tc-badge">{p['Asignatura']}</span><br>
                <strong>Nombre:</strong> {p['Nombre']} &nbsp;|&nbsp;
                <strong>Edad:</strong> {p['Edad']} &nbsp;|&nbsp;
                <strong>ID:</strong> {p['ID']}
            </div>
            """, unsafe_allow_html=True)
        st.caption(f"Total: {len(st.session_state.profesores)} profesor(es)")
    else:
        st.markdown('<div class="tc-empty">No hay profesores registrados.</div>', unsafe_allow_html=True)

# ── Matricular Estudiante ────────────────────────────────────────────────────
elif menu == "➕  Matricular Estudiante":
    st.markdown('<div class="tc-title">Matricular Estudiante</div>', unsafe_allow_html=True)

    with st.form("form_matricular"):
        nombre = st.text_input("Nombre completo")
        edad   = st.number_input("Edad", min_value=5, max_value=25, value=12)
        id_est = st.text_input("Número de identificación")
        grado  = st.selectbox("Grado", GRADOS)
        submit = st.form_submit_button("✅ Matricular")

    if submit:
        if nombre and id_est:
            ids_existentes = [e["ID"] for e in st.session_state.estudiantes]
            if id_est in ids_existentes:
                st.error("⚠️ Ya existe un estudiante con ese número de identificación.")
            else:
                st.session_state.estudiantes.append({
                    "Nombre": nombre, "Edad": int(edad),
                    "ID": id_est, "grado": grado
                })
                st.markdown('<div class="success-msg">✅ Estudiante matriculado exitosamente.</div>', unsafe_allow_html=True)
        else:
            st.error("⚠️ Por favor completa todos los campos.")

# ── Registrar Profesor ───────────────────────────────────────────────────────
elif menu == "➕  Registrar Profesor":
    st.markdown('<div class="tc-title">Registrar Profesor</div>', unsafe_allow_html=True)

    with st.form("form_profesor"):
        nombre     = st.text_input("Nombre completo")
        edad       = st.number_input("Edad", min_value=18, max_value=80, value=30)
        id_prof    = st.text_input("Número de identificación")
        asignatura = st.text_input("Asignatura a dictar")
        submit     = st.form_submit_button("✅ Registrar")

    if submit:
        if nombre and id_prof and asignatura:
            ids_existentes = [p["ID"] for p in st.session_state.profesores]
            if id_prof in ids_existentes:
                st.error("⚠️ Ya existe un profesor con ese número de identificación.")
            else:
                st.session_state.profesores.append({
                    "Nombre": nombre, "Edad": int(edad),
                    "ID": id_prof, "Asignatura": asignatura
                })
                st.markdown('<div class="success-msg">✅ Profesor registrado exitosamente.</div>', unsafe_allow_html=True)
        else:
            st.error("⚠️ Por favor completa todos los campos.")

# ── Expulsar Estudiante ──────────────────────────────────────────────────────
elif menu == "❌  Expulsar Estudiante":
    st.markdown('<div class="tc-title">Expulsar Estudiante</div>', unsafe_allow_html=True)

    grado_sel = st.selectbox("Selecciona el grado", GRADOS)
    lista = [e for e in st.session_state.estudiantes if e["grado"] == grado_sel]

    if lista:
        opciones = {f"{e['Nombre']} (ID: {e['ID']})": e["ID"] for e in lista}
        seleccion = st.selectbox("Selecciona el estudiante a expulsar", list(opciones.keys()))

        if st.button("❌ Confirmar expulsión"):
            id_sel = opciones[seleccion]
            st.session_state.estudiantes = [
                e for e in st.session_state.estudiantes if e["ID"] != id_sel
            ]
            st.markdown('<div class="success-msg">✅ Estudiante eliminado exitosamente.</div>', unsafe_allow_html=True)
            st.rerun()
    else:
        st.markdown('<div class="tc-empty">No hay estudiantes en este grado.</div>', unsafe_allow_html=True)

# ── Despedir Profesor ────────────────────────────────────────────────────────
elif menu == "❌  Despedir Profesor":
    st.markdown('<div class="tc-title">Despedir Profesor</div>', unsafe_allow_html=True)

    if st.session_state.profesores:
        opciones = {f"{p['Nombre']} — {p['Asignatura']} (ID: {p['ID']})": p["ID"] for p in st.session_state.profesores}
        seleccion = st.selectbox("Selecciona el profesor a despedir", list(opciones.keys()))

        if st.button("❌ Confirmar despido"):
            id_sel = opciones[seleccion]
            st.session_state.profesores = [
                p for p in st.session_state.profesores if p["ID"] != id_sel
            ]
            st.markdown('<div class="success-msg">✅ Profesor eliminado exitosamente.</div>', unsafe_allow_html=True)
            st.rerun()
    else:
        st.markdown('<div class="tc-empty">No hay profesores registrados.</div>', unsafe_allow_html=True)

# ── Actualizar Estudiante ────────────────────────────────────────────────────
elif menu == "✏️  Actualizar Estudiante":
    st.markdown('<div class="tc-title">Actualizar Estudiante</div>', unsafe_allow_html=True)

    grado_sel = st.selectbox("Selecciona el grado", GRADOS)
    lista = [e for e in st.session_state.estudiantes if e["grado"] == grado_sel]

    if lista:
        opciones = {f"{e['Nombre']} (ID: {e['ID']})": i for i, e in
                    enumerate(st.session_state.estudiantes) if e["grado"] == grado_sel}
        seleccion = st.selectbox("Selecciona el estudiante a actualizar", list(opciones.keys()))
        idx = opciones[seleccion]
        est = st.session_state.estudiantes[idx]

        with st.form("form_actualizar_est"):
            nuevo_nombre = st.text_input("Nuevo nombre", value=est["Nombre"])
            nueva_edad   = st.number_input("Nueva edad", min_value=5, max_value=25, value=est["Edad"])
            nueva_id     = st.text_input("Nuevo número de identificación", value=est["ID"])
            submit       = st.form_submit_button("✅ Actualizar")

        if submit:
            st.session_state.estudiantes[idx]["Nombre"] = nuevo_nombre
            st.session_state.estudiantes[idx]["Edad"]   = int(nueva_edad)
            st.session_state.estudiantes[idx]["ID"]     = nueva_id
            st.markdown('<div class="success-msg">✅ Estudiante actualizado exitosamente.</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="tc-empty">No hay estudiantes en este grado.</div>', unsafe_allow_html=True)

# ── Actualizar Profesor ──────────────────────────────────────────────────────
elif menu == "✏️  Actualizar Profesor":
    st.markdown('<div class="tc-title">Actualizar Profesor</div>', unsafe_allow_html=True)

    if st.session_state.profesores:
        opciones = {f"{p['Nombre']} — {p['Asignatura']} (ID: {p['ID']})": i
                    for i, p in enumerate(st.session_state.profesores)}
        seleccion = st.selectbox("Selecciona el profesor a actualizar", list(opciones.keys()))
        idx = opciones[seleccion]
        prof = st.session_state.profesores[idx]

        with st.form("form_actualizar_prof"):
            nuevo_nombre     = st.text_input("Nuevo nombre", value=prof["Nombre"])
            nueva_edad       = st.number_input("Nueva edad", min_value=18, max_value=80, value=prof["Edad"])
            nueva_id         = st.text_input("Nuevo número de identificación", value=prof["ID"])
            nueva_asignatura = st.text_input("Nueva asignatura", value=prof["Asignatura"])
            submit           = st.form_submit_button("✅ Actualizar")

        if submit:
            st.session_state.profesores[idx]["Nombre"]     = nuevo_nombre
            st.session_state.profesores[idx]["Edad"]       = int(nueva_edad)
            st.session_state.profesores[idx]["ID"]         = nueva_id
            st.session_state.profesores[idx]["Asignatura"] = nueva_asignatura
            st.markdown('<div class="success-msg">✅ Profesor actualizado exitosamente.</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="tc-empty">No hay profesores registrados.</div>', unsafe_allow_html=True)
