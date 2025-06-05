# Password Strength Checker 🔐

Este proyecto es una herramienta sencilla en Python para verificar la fortaleza de contraseñas, clasificándolas como **Débil**, **Media** o **Fuerte** según reglas de seguridad comunes. Incluye pruebas automatizadas y está listo para integrarse en flujos de CI/CD como GitHub Actions.

---

## 🚀 Características

- **Evaluación de contraseñas** según:
  - Longitud mínima de 8 caracteres.
  - Al menos una mayúscula.
  - Al menos una minúscula.
  - Al menos un dígito.
  - Al menos un símbolo (`@!$#*`).
  - Sin espacios.
- **Clasificación automática**:
  - **Fuerte**: Cumple longitud y al menos 3 requisitos extra.
  - **Media**: Cumple longitud y al menos 2 requisitos extra.
  - **Débil**: No cumple longitud o menos de 2 requisitos.
- **Pruebas unitarias** con `pytest`.
- **Preparado para CI/CD** (GitHub Actions).

---

## 📂 Estructura del proyecto

```
TallerCI-CD/
├── app/
│   ├── checker.py               # Lógica principal
├── tests/
│   └── test_checker.py          # Pruebas automatizadas
├── requirements.txt             # Dependencias
├── .github/
│   └── workflows/
│       └── CI-CD.yml               # GitHub Actions
├── .gitignore
└── README.md                    # Este archivo
```

---

## ⚙️ Instalación y uso

1. **Clona el repositorio**  
   ```bash
   git clone <https://github.com/BreyMene/BreynerMeneses1025888163.git>
   cd TallerCI-CD
   ```

2. **Instala las dependencias**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecuta el verificador**  
   ```bash
   python app/checker.py
   ```

---

## 🧪 Pruebas

Ejecuta las pruebas con:

```bash
PYTHONPATH=. pytest
```

---

## 🛠️ Personalización

Puedes modificar las reglas de seguridad en `app/checker.py` según tus necesidades.

---

## 🤖 CI/CD

El flujo de trabajo de GitHub Actions (`.github/workflows/ci.yml`) ejecuta automáticamente las pruebas en cada push o pull request.

## ✨ Autor

- Desarrollado por Breyner Meneses (BreyMene)
