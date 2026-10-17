import streamlit as st

# Konfiguracja strony
st.set_page_config(page_title="Bio-Energetic Training Advisor Pro", page_icon="⚡", layout="wide")

# Nagłówek główny aplikacji
st.title("⚡ Bio-Energetic Training Advisor Pro")
st.markdown("### Zaawansowany System Analizy Biochemicznej i Biomechanicznej Wysiłku Fizycznego")
st.markdown("---")

# Tworzenie zakładek (profesjonalny interfejs krok po kroku)
tab1, tab2, tab3, tab4 = st.tabs([
    "1️⃣ Profil i Aktywność", 
    "2️⃣ Mikroklimat Otoczenia", 
    "3️⃣ Biomechanika Mięśni", 
    "4️⃣ Raport i Protokół Regeneracji"
])

# Zmienne przechowujące stan (inicjalizizacja w pamięci sesji)
with tab1:
    st.header("Profil Biometryczny i Rodzaj Wysiłku")
    col1, col2 = st.columns(2)
    with col1:
        waga = st.number_input("Waga ciała (kg):", min_value=30.0, max_value=160.0, value=65.0, step=0.5)
        wiek = st.number_input("Wiek:", min_value=12, max_value=90, value=17)
    with col2:
        aktywnosc = st.selectbox(
            "Wybierz główny profil aktywności:", 
            [
                "Trening oporowy / Siłowy (Hipertrofia)", 
                "Bieganie interwałowe / Szybkościowe", 
                "Trening tlenowy / Długi spacer", 
                "Sport zespołowy (Piłka nożna/koszykówka)"
            ]
        )
        czas = st.slider("Czas trwania wysiłku (w minutach):", min_value=15, max_value=240, value=60, step=5)

with tab2:
    st.header("Analiza Mikroklimatu i Termoregulacji")
    st.markdown("Warunki środowiskowe drastycznie zmieniają wydatkowanie energii oraz mechanizmy pocenia się.")
    
    col_t1, col_t2 = st.columns(2)
    with col_t1:
        temp = st.slider("Temperatura otoczenia (°C):", min_value=0.0, max_value=45.0, value=22.0, step=0.5)
    with col_t2:
        wilgotnosc = st.slider("Wilgotność względna powietrza (%):", min_value=10, max_value=100, value=50, step=1)
        
    # Informacja naukowa wyświetlana dynamicznie
    if wilgotnosc > 70 and temp > 22:
        st.error("⚠️ **Wysoki wskaźnik obciążenia termicznego!** Parowanie potu jest mocno utrudnione, co drastycznie zwiększa tętno submaksymalne oraz utratę elektrolitów.")
    elif wilgotnosc < 30:
        st.warning("⚠️ **Niska wilgotność:** Ryzyko szybkiego odwodnienia przez przyspieszone odparowywanie potu z dróg oddechowych i skóry.")
    else:
        st.success("✅ **Optymalne warunki środowiskowe** dla umiarkowanego wysiłku fizycznego.")

with tab3:
    st.header("Mapa Zaangażowania Biomechanicznego Mięśni")
    st.markdown("Wybierz partie mięśniowe, które były poddane największym obciążeniom mechanicznym:")
    
    partie_wybrane = st.multiselect(
        "Główne grupy mięśniowe:",
        [
            "Mięśnie czworogłowe ud (przód nóg)",
            "Mięśnie dwugłowe ud i pośladki (tył taśmy biodrowej)",
            "Kompleks mięśni brzucha i core (tułów)",
            "Klatka piersiowa",
            "Grzbiet / Prostowniki grzbietu",
            "Kończyny górne (Biceps / Triceps / Barki)",
            "Łydki i stawy skokowe"
        ],
        default=["Mięśnie czworogłowe ud (przód nóg)", "Mięśnie dwugłowe ud i pośladki (tył taśmy biodrowej)"]
    )
    
    intensywnosc_rpe = st.select_slider(
        "Subiektywna skala odczuwanego wysiłku (RPE / Skala Borga):",
        options=["Niska (1-3)", "Umiarkowana (4-6)", "Wysoka (7-8)", "Maksymalna / Startowa (9-10)"]
    )

with tab4:
    st.header("Algorytmiczny Raport Biochemiczny i Regeneracyjny")
    st.markdown("Przejdź do tej zakładki, aby wygenerować pełny profil zapotrzebowania organizmu.")
    
    if st.button("🚀 Oblicz Zaawansowany Profil Biochemiczny", type="primary"):
        
        # 1. Zaawansowane obliczenia fizjologiczne
        mnoznik_intensywnosci = {
            "Niska (1-3)": 0.7, 
            "Umiarkowana (4-6)": 1.0, 
            "Wysoka (7-8)": 1.35, 
            "Maksymalna / Startowa (9-10)": 1.7
        }[intensywnosc_rpe]
        
        # Wpływ temperatury i wilgotności na współczynnik potliwości
        wsp_termiczny = 1.0 + max(0.0, (temp - 20) * 0.02) + max(0.0, (wilgotnosc - 50) * 0.005)
        
        # Utrata wody w mililitrach
        bazowa_utrata_wody = czas * 10 * (waga / 70.0)
        calkowita_woda = int(bazowa_utrata_wody * mnoznik_intensywnosci * wsp_termiczny)
        
        # Utrata sodu (mg) rośnie wraz z potem i wilgotnością
        sod_mg = int(calkowita_woda * 0.65 * (wilgotnosc / 40.0 if wilgotnosc > 40 else 1.0))
        
        # Zużycie glikogenu (g) w zależności od typu aktywności
        wsp_glikogenu = 1.2 if "siłowy" in aktywnosc else 1.8
        zuzycie_glikogenu = int(czas * wsp_glikogenu * mnoznik_intensywnosci * (waga / 70.0))
        
        # Czas regeneracji mięśni
        czas_reg = "36 - 48 godzin" if "siłowy" in aktywnosc else "24 godziny"
        if "Maksymalna" in intensywnosc_rpe:
            czas_reg = "72 godziny (wymagana superkompensacja białkowa)"

        # Wyświetlanie wyników w nowoczesnych kafelkach
        col_res1, col_res2, col_res3 = st.columns(3)
        col_res1.metric(label="💧 Zapotrzebowanie H₂O", value=f"{calkowita_woda} ml", delta=f"+{int((wsp_termiczny-1)*100)}% stresu termicznego")
        col_res2.metric(label="🧂 Utrata Sodu (Na⁺)", value=f"{sod_mg} mg", delta="Elektrolity kluczowe")
        col_res3.metric(label="⛽ Odbudowa Glikogenu", value=f"{zuzycie_glikogenu} g", delta="Węglowodany")
        
        st.divider()
        
        # Szczegółowe rekomendacje
        st.subheader("📋 Indywidualny Plan Odbudowy Biochemicznej")
        
        st.info(f"💪 **Analiza mikrourazów mięśniowych:** Aktywność obciążyła następujące struktury: **{', '.join(partie_wybrane) if partie_wybrane else 'Brak zaznaczonych'}**. Szacowany czas pełnej regeneracji włókien mięśniowych wynosi: **{czas_reg}**.")
        
        st.success(f"🧪 **Przepis na spersonalizowany roztwór izotoniczny:** Wymieszaj **{calkowita_woda} ml czystej wody** z **{round(sod_mg/1000.0, 2)} g soli kuchennej**, dodaj sok z połowy cytryny oraz **{max(20, int(zuzycie_glikogenu/4))} g miodu lub maltodekstryny**, aby błyskawicznie uzupełnić puste magazyny glikogenu.")