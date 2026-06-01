# Contributing

Usamos **trunk-based development** — ramas cortas, una por clase, cualquiera puede tomar cualquier clase. Nadie es dueño de nada.

## Flujo por clase

**1. Arrancar siempre desde main actualizado**
```bash
git checkout main
git pull origin main
git checkout -b feat/nombre-clase
```

**2. Escribir test → implementar → pasar tests**
```bash
pytest
```

**3. Commitear y subir**
```bash
git add .
git commit -m "feat: clase NombreClase"
git push origin feat/nombre-clase
```

**4. Abrir Pull Request en GitHub**
- Ir al repo → "Compare & pull request"
- Título claro, descripción de qué hiciste
- El que NO escribió la clase aprueba el PR

**5. Merge y repetir**
- Main está protegido — merge bloqueado hasta que el otro apruebe.
- Después del merge, volver al paso 1 para la siguiente clase.

## Reglas

- Una rama = una clase = un PR
- La rama vive máximo 1-2 horas, nunca overnight
- Antes de cada rama nueva: `git pull origin main`
- Cualquiera puede tomar cualquier clase
