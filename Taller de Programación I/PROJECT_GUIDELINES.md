# Directrices del Repositorio: Taller de Programación I (USS)

Este documento establece las reglas de organización, estándares de codificación y flujos de trabajo que deben respetar todos los agentes de IA y colaboradores que participen en el desarrollo y mantenimiento de este proyecto de programación.

---

## 📂 Estructura del Repositorio

El repositorio está organizado por unidades académicas del curso de la Universidad San Sebastián (USS):

```text
Taller de Programación I/
│
├── Unidad 1/
│   ├── Pseudocódigo y algoritmos/      # Ejercicios y lógica en pseudocódigo y diagramas de flujo.
│   └── Extra - Python/                 # Scripts de introducción a la sintaxis básica de Python.
│
├── Unidad 2/
│   ├── Documentación/                  # Diapositivas, programas del ramo y apuntes de clases en PDF/Markdown.
│   ├── Guías/                          # Enunciados oficiales de las guías prácticas (Guías 1 a 4, etc.).
│   └── Guías resueltas/                # Soluciones oficiales e implementaciones en Python de los ejercicios.
│
└── PROJECT_GUIDELINES.md               # Este archivo (Directrices y estándares).
```

---

## 🐍 Estándares de Codificación en Python

Para asegurar que todo el código sea legible, mantenible y coherente con las prácticas académicas:

1. **Versión de Python**: Utilizar Python 3.10 o superior.
2. **Estilo de Formato (PEP 8)**:
   * Sangrado de 4 espacios (no usar tabuladores).
   * Límites de línea razonables (~79-88 caracteres).
   * Una línea en blanco antes de funciones y dos líneas en blanco antes de clases.
3. **Nombramiento**:
   * Usar nombres descriptivos en **español** para variables y funciones (ej. `calcular_promedio` en lugar de `calc_prom`).
   * **Variables/Funciones**: `snake_case` (ej. `nota_final`).
   * **Constantes**: `UPPER_SNAKE_CASE` (ej. `IVA_VALOR`).
4. **Comentarios y Documentación**:
   * Escribir docstrings en funciones complejas detallando parámetros y retornos.
   * Usar comentarios en español de manera estratégica para explicar lógica matemática o algorítmica no trivial (evitar redundancias como `# incrementar i en 1`).
   * **Preservación**: Conservar comentarios y docstrings originales que no sean objeto de modificación directa.
5. **Robustez**:
   * Validar las entradas de usuario en programas interactivos (ej. control de excepciones ante entradas incorrectas).
   * No utilizar placeholders o código incompleto (`pass`, `TODO` sin resolver). Todo el código propuesto debe ser funcional y ejecutable de inmediato.

---

## 🔄 Integración con el Sistema de Conocimiento (Obsidian)

El repositorio de código está sincronizado con la bóveda personal de Obsidian ubicada en:
`/mnt/9b846436-0407-4e80-b8af-5417ffbdee8e/ObsidianVault/Proyectos/Taller_Programacion_I/`

Cualquier cambio realizado en este repositorio (ej. resolución de una guía, análisis de errores) debe sincronizarse en Obsidian siguiendo estas reglas:
* **Guías y Código**: Cada guía resuelta debe tener su correspondiente nota explicativa en `Knowledge/` con un análisis de la lógica utilizada y casos de prueba.
* **Bitácora de Progreso**: Registrar hitos y resúmenes de sesión en `Logs/execution_logs.md`.
* **Metadatos YAML**: Mantener el frontmatter de Obsidian actualizado con la fecha actual y las etiquetas del proyecto.

---

## 🛠️ Control de Versiones (Git)

* Realizar confirmaciones (*commits*) atómicos y auto-explicativos.
* Utilizar una estructura clara para los mensajes de commit:
  * `feat(u2): resolver ejercicio 4 de guía 3`
  * `docs(u2): agregar apuntes de la clase de arreglos`
  * `fix(u1): corregir bug en validador de entrada en script de cálculo`

---

> **Nota para Agentes**: Este archivo es la fuente de la verdad para el desarrollo en este repositorio. Cualquier script, tarea o sugerencia de código debe adecuarse estrictamente a estas reglas.
