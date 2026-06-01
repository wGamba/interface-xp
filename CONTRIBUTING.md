# Contributing

## Flujo de trabajo

**1. Crear rama desde main**
```bash
git checkout main
git pull origin main
git checkout -b ariel/nombre-feature
```

**2. Trabajar y commitear**
```bash
git add archivo.py
git commit -m "feat: descripción corta"
git push origin ariel/nombre-feature
```

**3. Abrir Pull Request en GitHub**
- Ir al repo → "Compare & pull request"
- Título claro, descripción de qué hiciste
- Asignar reviewer: **wGamba**

**4. Esperar aprobación**
- Main está protegido — el merge está bloqueado hasta que el otro integrante apruebe.
- No hace falta hacer nada más, GitHub lo maneja.

**5. Después del merge, actualizar local**
```bash
git checkout main
git pull origin main
```
