import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from sympy import symbols, diff, latex, sympify, simplify
import plotly.graph_objects as go
from PIL import Image

# Konfigurasi halaman
st.set_page_config(
    page_title="Aplikasi Fungsi Matematika & Optimasi",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =================== GEN-Z MODERN NEON THEME CSS ===================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

/* Main App Background */
.stApp {
    background: radial-gradient(circle at 20% 30%, #7f5af0, #2cb67d 40%, #16161a 90%);
    background-attachment: fixed;
    color: #fffffe;
}

/* Title Styling */
h1 {
    font-weight: 900;
    font-size: 3rem;
    text-align: center;
    background: linear-gradient(90deg, #2cb67d, #7f5af0, #00c6ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    letter-spacing: 3px;
    animation: glow 2s ease-in-out infinite alternate;
}

@keyframes glow {
  from { text-shadow: 0 0 10px rgba(255,255,255,0.3); }
  to { text-shadow: 0 0 25px rgba(255,255,255,0.7); }
}

h2, h3 {
    color: #fffffe;
    font-weight: 700;
}

/* Cards - Glassmorphism */
div[data-testid="stHorizontalBlock"] > div {
    background: rgba(255,255,255,0.08);
    padding: 25px;
    border-radius: 20px;
    border: 1px solid rgba(255,255,255,0.15);
    box-shadow: 0 10px 35px rgba(0,0,0,0.35);
    backdrop-filter: blur(15px);
    transition: transform 0.25s ease, box-shadow 0.25s ease;
}

div[data-testid="stHorizontalBlock"] > div:hover {
    transform: translateY(-6px);
    box-shadow: 0 16px 45px rgba(0,0,0,0.5);
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: rgba(22, 22, 26, 0.45);
    backdrop-filter: blur(20px);
    border-right: 1px solid rgba(255,255,255,0.15);
}

/* Navigation Radio Buttons */
.stRadio > div {
    background: rgba(255,255,255,0.1);
    padding: 15px;
    border-radius: 15px;
}

/* Buttons - RGB neon hover */
.stButton > button {
    background: linear-gradient(135deg, #7f5af0, #2cb67d);
    color: white;
    border-radius: 15px;
    border: none;
    font-weight: 700;
    padding: 0.7rem 2rem;
    transition: 0.3s ease;
    box-shadow: 0 0 15px rgba(127, 90, 240, 0.6);
}

.stButton > button:hover {
    transform: scale(1.08) translateY(-4px);
    box-shadow: 0 0 25px rgba(44, 182, 125, 0.8);
    background: linear-gradient(135deg, #00c6ff, #7f5af0);
}

/* Input Box */
.stTextInput > div > input {
    background: rgba(255,255,255,0.15);
    padding: 12px;
    border-radius: 12px;
    color: white;
    border: 1px solid rgba(255,255,255,0.15);
}

/* Expander */
.streamlit-expanderHeader {
    color: #2cb67d;
    font-weight: 600;
}

/* Plot graphs frame */
.plotly-graph-div {
    border-radius: 18px;
    overflow: hidden;
    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
}

</style>
""", unsafe_allow_html=True)

# Sidebar navigasi
st.sidebar.title("📐 Navigasi")
halaman = st.sidebar.radio(
    "Pilih Halaman:",
    ["🏠 Beranda", "👥 Anggota Tim", "📈 Analisis Fungsi", "🎯 Pemecah Optimasi"]
)

# ================== HALAMAN 1: BERANDA ==================
if halaman == "🏠 Beranda":
    st.title("🎓 Aplikasi Web Fungsi Matematika & Optimasi")
    st.markdown("### Platform Alat Kalkulus Lanjutan & Pemecahan Masalah")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style='background: white; padding: 2rem; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);'>
            <h3 style='text-align: center;'>👥 Anggota Tim</h3>
            <p style='text-align: center; color: #6b7280;'>Kenali tim pengembang dan kontribusi mereka</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style='background: white; padding: 2rem; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);'>
            <h3 style='text-align: center;'>📈 Analisis Fungsi</h3>
            <p style='text-align: center; color: #6b7280;'>Visualisasikan fungsi dan hitung turunannya</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style='background: white; padding: 2rem; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);'>
            <h3 style='text-align: center;'>🎯 Optimasi</h3>
            <p style='text-align: center; color: #6b7280;'>Selesaikan soal cerita langkah demi langkah</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 🚀 Fitur-fitur")
    st.markdown("""
    - ✅ *Visualisasi Fungsi*: Plot fungsi matematika apapun
    - ✅ *Komputasi Turunan*: Diferensiasi langkah demi langkah dengan tampilan LaTeX
    - ✅ *Pemecah Optimasi*: Selesaikan masalah optimasi dunia nyata
    - ✅ *Plot Interaktif*: Visualisasi dinamis dan responsif
    """)

# ================== HALAMAN 2: ANGGOTA TIM ==================
elif halaman == "👥 Anggota Tim":
    st.title("👥 Tim Pengembang Kami")
    st.markdown("### Kenali orang-orang di balik proyek ini")
    
    col1, col2, col3 = st.columns(3)
    
    # Anggota tim 1
    with col1:
        st.markdown("""
        <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    padding: 3rem; border-radius: 15px; text-align: center; color: white;'>
            <div style='width: 120px; height: 120px; background: white; border-radius: 50%; 
                        margin: 0 auto 1rem; display: flex; align-items: center; 
                        justify-content: center; font-size: 3rem; color: #667eea;'>
                👨‍💻
            </div>
            <h3>Rasyid Irvan Maulana</h3>
            <p style='font-weight: bold; color: #fbbf24;'>Ketua Proyek & Pengembang Backend</p>
            <p style='font-size: 0.9rem;'>Integrasi API, algoritma turunan, arsitektur sistem</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Anggota tim 2
    with col2:
        st.markdown("""
        <div style='background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); 
                    padding: 3rem; border-radius: 15px; text-align: center; color: white;'>
            <div style='width: 120px; height: 120px; background: white; border-radius: 50%; 
                        margin: 0 auto 1rem; display: flex; align-items: center; 
                        justify-content: center; font-size: 3rem; color: #f5576c;'>
                👩‍💻
            </div>
            <h3>Luthfi Ilham Pratama</h3>
            <p style='font-weight: bold; color: #fbbf24;'>Pengembang Frontend</p>
            <p style='font-size: 0.9rem;'>Desain UI/UX, komponen Streamlit, visualisasi</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Anggota tim 3
    with col3:
        st.markdown("""
        <div style='background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); 
                    padding: 3rem; border-radius: 15px; text-align: center; color: white;'>
            <div style='width: 120px; height: 120px; background: white; border-radius: 50%; 
                        margin: 0 auto 1rem; display: flex; align-items: center; 
                        justify-content: center; font-size: 3rem; color: #00f2fe;'>
                👩‍🔬
            </div>
            <h3>Andrian Ramadhan</h3>
            <p style='font-weight: bold; color: #fbbf24;'>Spesialis Matematika</p>
            <p style='font-size: 0.9rem;'>Algoritma optimasi, validasi matematis, pengujian</p>
        </div>
        """, unsafe_allow_html=True)

           # Anggota tim 4
    with col3:
        st.markdown("""
        <div style='background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); 
                    padding: 3rem; border-radius: 15px; text-align: center; color: white;'>
            <div style='width: 120px; height: 120px; background: white; border-radius: 50%; 
                        margin: 0 auto 1rem; display: flex; align-items: center; 
                        justify-content: center; font-size: 3rem; color: #00f2fe;'>
                👩‍🔬
            </div>
            <h3>Riska Dwi</h3>
            <p style='font-weight: bold; color: #fbbf24;'>Spesialis Matematika</p>
            <p style='font-size: 0.9rem;'>Algoritma optimasi, validasi matematis, pengujian</p>
        </div>
        """, unsafe_allow_html=True)

# ================== HALAMAN 3: ANALISIS FUNGSI ==================
elif halaman == "📈 Analisis Fungsi":
    st.title("📈 Visualisasi Fungsi & Diferensiasi")
    
    # Input fungsi
    st.markdown("### 🔢 Masukkan Fungsi Matematika")
    col1, col2 = st.columns([3, 1])
    
    with col1:
        input_fungsi = st.text_input(
            "Fungsi (gunakan x sebagai variabel):",
            value="x**2 + 3*x + 2",
            help="Contoh: x*2, sin(x), exp(x), x*3 - 2*x"
        )
    
    with col2:
        rentang_x = st.slider("Rentang Plot", -20, 20, (-10, 10))
    
    try:
        # Parse fungsi
        x = symbols('x')
        ekspresi_fungsi = sympify(input_fungsi)
        
        # Tampilkan fungsi dalam LaTeX
        st.markdown("### 📝 Tampilan Fungsi")
        st.latex(f"f(x) = {latex(ekspresi_fungsi)}")
        
        # Hitung turunan
        if st.button("🧮 Hitung Turunan", key="hitung_turunan"):
            st.markdown("---")
            st.markdown("### 📊 Turunan Langkah demi Langkah")
            
            # Tampilkan langkah-langkah diferensiasi
            turunan = diff(ekspresi_fungsi, x)
            
            with st.expander("📖 Langkah-langkah Diferensiasi", expanded=True):
                st.markdown("*Langkah 1:* Identifikasi fungsi yang akan diturunkan")
                st.latex(f"f(x) = {latex(ekspresi_fungsi)}")
                
                st.markdown("*Langkah 2:* Terapkan aturan diferensiasi")
                
                # Cek tipe fungsi
                if ekspresi_fungsi.is_polynomial():
                    st.markdown("- Menggunakan *Aturan Pangkat*: $\\frac{d}{dx}[x^n] = nx^{n-1}$")
                if ekspresi_fungsi.has(sp.sin) or ekspresi_fungsi.has(sp.cos):
                    st.markdown("- Menggunakan *Aturan Trigonometri*")
                if ekspresi_fungsi.has(sp.exp):
                    st.markdown("- Menggunakan *Aturan Eksponensial*: $\\frac{d}{dx}[e^x] = e^x$")
                
                st.markdown("*Langkah 3:* Sederhanakan hasilnya")
                turunan_sederhana = simplify(turunan)
                
                st.markdown("*Langkah 4:* Turunan akhir")
                st.latex(f"f'(x) = {latex(turunan_sederhana)}")
            
            # Tampilkan hasil akhir dengan menonjol
            st.success("✅ Turunan Berhasil Dihitung!")
            st.markdown("### 🎯 Hasil Akhir")
            st.latex(f"\\boxed{{f'(x) = {latex(turunan_sederhana)}}}")
            
            # Plot fungsi asli dan turunan
            st.markdown("---")
            st.markdown("### 📊 Visualisasi")
            
            col1, col2 = st.columns(2)
            
            # Plot fungsi asli
            with col1:
                st.markdown("#### Fungsi Asli f(x)")
                nilai_x = np.linspace(rentang_x[0], rentang_x[1], 400)
                f_lambda = sp.lambdify(x, ekspresi_fungsi, 'numpy')
                
                try:
                    nilai_y = f_lambda(nilai_x)
                    
                    fig1 = go.Figure()
                    fig1.add_trace(go.Scatter(
                        x=nilai_x, y=nilai_y,
                        mode='lines',
                        name='f(x)',
                        line=dict(color='#667eea', width=3)
                    ))
                    fig1.update_layout(
                        title="Fungsi Asli",
                        xaxis_title="x",
                        yaxis_title="f(x)",
                        hovermode='x',
                        template='plotly_white'
                    )
                    st.plotly_chart(fig1, use_container_width=True)
                except:
                    st.error("Tidak dapat memplot fungsi ini dalam rentang yang diberikan")
            
            # Plot turunan
            with col2:
                st.markdown("#### Turunan f'(x)")
                turunan_lambda = sp.lambdify(x, turunan, 'numpy')
                
                try:
                    nilai_dy = turunan_lambda(nilai_x)
                    
                    fig2 = go.Figure()
                    fig2.add_trace(go.Scatter(
                        x=nilai_x, y=nilai_dy,
                        mode='lines',
                        name="f'(x)",
                        line=dict(color='#f5576c', width=3)
                    ))
                    fig2.update_layout(
                        title="Fungsi Turunan",
                        xaxis_title="x",
                        yaxis_title="f'(x)",
                        hovermode='x',
                        template='plotly_white'
                    )
                    st.plotly_chart(fig2, use_container_width=True)
                except:
                    st.error("Tidak dapat memplot turunan dalam rentang yang diberikan")
    
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")
        st.info("Silakan masukkan ekspresi matematika yang valid. Contoh: x**2, sin(x), exp(x)")

# ================== HALAMAN 4: OPTIMASI ==================
elif halaman == "🎯 Pemecah Optimasi":
    st.title("🎯 Pemecah Soal Cerita Optimasi")
    
    st.markdown("### 📝 Masukkan Masalah Optimasi Anda")
    
    # Contoh masalah yang telah ditentukan
    contoh_masalah = {
        "Luas Persegi Panjang (Kendala Keliling)": {
            "masalah": "Seorang petani memiliki 40 meter pagar untuk memagari area persegi panjang. Dimensi apa yang akan memaksimalkan luas yang dipagari?",
            "tipe_solusi": "persegi_panjang_keliling"
        },
        "Volume Kotak (Luas Permukaan)": {
            "masalah": "Sebuah kotak terbuka dibuat dari selembar karton persegi berukuran 12 inci pada setiap sisi dengan memotong persegi yang sama dari sudut dan melipat sisi ke atas. Temukan ukuran persegi sudut yang memaksimalkan volume.",
            "tipe_solusi": "volume_kotak"
        },
        "Optimasi Produk": {
            "masalah": "Temukan dua bilangan positif yang jumlahnya 50 dan produknya maksimum.",
            "tipe_solusi": "jumlah_produk"
        }
    }
    
    pilihan_contoh = st.selectbox(
        "Pilih contoh atau masukkan sendiri:",
        ["Masalah Kustom"] + list(contoh_masalah.keys())
    )
    
    if pilihan_contoh == "Masalah Kustom":
        teks_masalah = st.text_area(
            "Masukkan soal cerita:",
            height=150,
            placeholder="Deskripsikan masalah optimasi Anda di sini..."
        )
    else:
        teks_masalah = st.text_area(
            "Masalah:",
            value=contoh_masalah[pilihan_contoh]["masalah"],
            height=150
        )
    
    if st.button("🔍 Selesaikan Masalah Optimasi"):
        if teks_masalah:
            st.markdown("---")
            st.markdown("### 🧮 Solusi")
            
            # Selesaikan berdasarkan tipe contoh
            if pilihan_contoh == "Luas Persegi Panjang (Kendala Keliling)":
                with st.expander("📋 Solusi Langkah demi Langkah", expanded=True):
                    st.markdown("*Langkah 1: Definisikan Variabel*")
                    st.markdown("- Misalkan $x$ = panjang persegi panjang")
                    st.markdown("- Misalkan $y$ = lebar persegi panjang")
                    st.markdown("- Kendala keliling: $2x + 2y = 40$")
                    
                    st.markdown("*Langkah 2: Ekspresikan Fungsi Objektif*")
                    st.markdown("- Objektif: Maksimalkan Luas $A = xy$")
                    st.markdown("- Dari kendala: $y = 20 - x$")
                    st.markdown("- Substitusi: $A(x) = x(20-x) = 20x - x^2$")
                    st.latex("A(x) = 20x - x^2")
                    
                    st.markdown("*Langkah 3: Temukan Titik Kritis*")
                    st.markdown("- Ambil turunan: $A'(x) = 20 - 2x$")
                    st.latex("A'(x) = 20 - 2x")
                    st.markdown("- Set sama dengan nol: $20 - 2x = 0$")
                    st.markdown("- Selesaikan: $x = 10$")
                    
                    st.markdown("*Langkah 4: Verifikasi Maksimum*")
                    st.markdown("- Turunan kedua: $A''(x) = -2 < 0$ (cekung ke bawah)")
                    st.markdown("- Oleh karena itu, $x = 10$ memberikan maksimum")
                    st.markdown("- Ketika $x = 10$: $y = 20 - 10 = 10$")
                    
                    st.markdown("*Langkah 5: Hitung Luas Maksimum*")
                    st.markdown("- Luas Maksimum = $10 \\times 10 = 100$ meter persegi")
                
                st.success("✅ *Solusi:* Persegi panjang harus berbentuk persegi dengan sisi 10 meter masing-masing, memberikan luas maksimum 100 meter persegi.")
                
                # Plot
                st.markdown("### 📊 Visualisasi")
                nilai_x = np.linspace(0, 20, 200)
                nilai_luas = nilai_x * (20 - nilai_x)
                
                fig = go.Figure()
                fig.add_trace(go.Scatter(
                    x=nilai_x, y=nilai_luas,
                    mode='lines',
                    name='Luas',
                    line=dict(color='#667eea', width=3)
                ))
                fig.add_trace(go.Scatter(
                    x=[10], y=[100],
                    mode='markers',
                    name='Maksimum',
                    marker=dict(color='red', size=15, symbol='star')
                ))
                fig.update_layout(
                    title="Luas vs. Panjang",
                    xaxis_title="Panjang (x) dalam meter",
                    yaxis_title="Luas dalam meter persegi",
                    hovermode='x',
                    template='plotly_white'
                )
                st.plotly_chart(fig, use_container_width=True)
            
            elif pilihan_contoh == "Optimasi Produk":
                with st.expander("📋 Solusi Langkah demi Langkah", expanded=True):
                    st.markdown("*Langkah 1: Definisikan Variabel*")
                    st.markdown("- Misalkan $x$ = bilangan pertama")
                    st.markdown("- Misalkan $y$ = bilangan kedua")
                    st.markdown("- Kendala: $x + y = 50$")
                    
                    st.markdown("*Langkah 2: Ekspresikan Fungsi Objektif*")
                    st.markdown("- Objektif: Maksimalkan Produk $P = xy$")
                    st.markdown("- Dari kendala: $y = 50 - x$")
                    st.markdown("- Substitusi: $P(x) = x(50-x) = 50x - x^2$")
                    
                    st.markdown("*Langkah 3: Temukan Titik Kritis*")
                    st.markdown("- Turunan: $P'(x) = 50 - 2x$")
                    st.markdown("- Set ke nol: $x = 25$")
                    
                    st.markdown("*Langkah 4: Verifikasi dan Hitung*")
                    st.markdown("- Ketika $x = 25$: $y = 25$")
                    st.markdown("- Produk Maksimum = $25 \\times 25 = 625$")
                
                st.success("✅ *Solusi:* Kedua bilangan adalah 25 dan 25, dengan produk maksimum 625.")
                
                # Plot
                nilai_x = np.linspace(0, 50, 200)
                nilai_produk = nilai_x * (50 - nilai_x)
                
                fig = go.Figure()
                fig.add_trace(go.Scatter(
                    x=nilai_x, y=nilai_produk,
                    mode='lines',
                    name='Produk',
                    line=dict(color='#f5576c', width=3)
                ))
                fig.add_trace(go.Scatter(
                    x=[25], y=[625],
                    mode='markers',
                    name='Maksimum',
                    marker=dict(color='green', size=15, symbol='star')
                ))
                fig.update_layout(
                    title="Produk vs. Bilangan Pertama",
                    xaxis_title="Bilangan Pertama (x)",
                    yaxis_title="Produk (xy)",
                    template='plotly_white'
                )
                st.plotly_chart(fig, use_container_width=True)
            
            elif pilihan_contoh == "Volume Kotak (Luas Permukaan)":
                with st.expander("📋 Solusi Langkah demi Langkah", expanded=True):
                    st.markdown("*Langkah 1: Definisikan Variabel*")
                    st.markdown("- Misalkan $x$ = panjang sisi persegi yang dipotong (inci)")
                    st.markdown("- Ukuran karton asli: 12 × 12 inci")
                    st.markdown("- Setelah dipotong: panjang alas = $(12-2x)$, lebar = $(12-2x)$, tinggi = $x$")
                    
                    st.markdown("*Langkah 2: Ekspresikan Fungsi Volume*")
                    st.markdown("- Volume: $V = (12-2x)(12-2x)(x)$")
                    st.markdown("- $V(x) = x(12-2x)^2 = x(144 - 48x + 4x^2)$")
                    st.markdown("- $V(x) = 4x^3 - 48x^2 + 144x$")
                    st.latex("V(x) = 4x^3 - 48x^2 + 144x")
                    
                    st.markdown("*Langkah 3: Temukan Titik Kritis*")
                    st.markdown("- Turunan: $V'(x) = 12x^2 - 96x + 144$")
                    st.markdown("- Set ke nol: $12x^2 - 96x + 144 = 0$")
                    st.markdown("- Sederhanakan: $x^2 - 8x + 12 = 0$")
                    st.markdown("- Faktorkan: $(x-2)(x-6) = 0$")
                    st.markdown("- Solusi: $x = 2$ atau $x = 6$")
                    
                    st.markdown("*Langkah 4: Tentukan Maksimum*")
                    st.markdown("- Untuk $x = 6$: dimensi alas = $12-2(6) = 0$ (tidak valid)")
                    st.markdown("- Untuk $x = 2$: dimensi alas = $12-2(2) = 8$ inci")
                    st.markdown("- Turunan kedua: $V''(2) = 24(2) - 96 = -48 < 0$ (maksimum)")
                    
                    st.markdown("*Langkah 5: Hitung Volume Maksimum*")
                    st.markdown("- Volume maksimum = $2 \\times 8 \\times 8 = 128$ inci kubik")
                
                st.success("✅ *Solusi:* Potong persegi 2 inci × 2 inci dari setiap sudut untuk mendapatkan volume maksimum 128 inci kubik.")
                
                # Plot
                nilai_x = np.linspace(0.1, 6, 200)
                nilai_volume = 4*nilai_x*3 - 48*nilai_x*2 + 144*nilai_x
                
                fig = go.Figure()
                fig.add_trace(go.Scatter(
                    x=nilai_x, y=nilai_volume,
                    mode='lines',
                    name='Volume',
                    line=dict(color='#9333ea', width=3)
                ))
                fig.add_trace(go.Scatter(
                    x=[2], y=[128],
                    mode='markers',
                    name='Maksimum',
                    marker=dict(color='red', size=15, symbol='star')
                ))
                fig.update_layout(
                    title="Volume vs. Ukuran Potongan",
                    xaxis_title="Ukuran Potongan Sudut (x) dalam inci",
                    yaxis_title="Volume dalam inci kubik",
                    template='plotly_white'
                )
                st.plotly_chart(fig, use_container_width=True)
            
            else:
                st.info("💡 Untuk masalah kustom, silakan pilih salah satu contoh yang telah ditentukan untuk melihat format solusi.")
        else:
            st.warning("⚠ Silakan masukkan masalah untuk diselesaikan.")

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("### 📚 Tentang")
st.sidebar.info("""
Aplikasi ini mendemonstrasikan:
- Visualisasi fungsi
- Diferensiasi simbolik
- Pemecahan masalah optimasi
- Alat matematika interaktif
""")

st.sidebar.markdown("### 🛠 Teknologi")
st.sidebar.markdown("""
- Python
- Streamlit
- SymPy
- Plotly
- NumPy
""")
