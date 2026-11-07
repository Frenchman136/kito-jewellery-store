"""Generates original SVG product images + supabase/seed.sql. Run: python3 scripts/generate_assets.py
All artwork is drawn from simple shapes here, so there are no third-party assets."""
import os

METALS = {
    "silver": ("#F7F7F7", "#8F8F8F"),
    "gold":   ("#F3D58B", "#B8893B"),
    "rose":   ("#F0C9BC", "#B7796A"),
}

# slug, name, category, price(KES), material, metal, style, stock, description
P = [
 ("sol-signet-ring","Sol Signet Ring","rings",4200,"925 sterling silver","silver","signet",8,
  "A small, smooth signet ring with a softly domed face. It sits comfortably on the little finger or index finger and pairs well with stacking bands. Polished by hand and finished with a light satin edge."),
 ("twist-stacking-ring","Twist Stacking Ring","rings",3800,"18k gold-plated sterling silver","gold","twist",3,
  "A slim twisted band made to be worn alone or stacked with others. The rope texture catches the light without feeling busy, and the thin profile stays comfortable through a full day of wear."),
 ("moonstone-band-ring","Moonstone Band Ring","rings",5600,"925 sterling silver, moonstone","silver","stone",0,
  "A plain band set with a single milky moonstone. The stone flashes a pale blue glow in daylight. Currently sold out, check back soon for the next small batch."),
 ("petal-pendant-necklace","Petal Pendant Necklace","necklaces",6900,"18k gold-plated sterling silver","gold","petal",12,
  "A fine chain with a single petal-shaped pendant that rests just below the collarbone. Light enough to forget you are wearing it, and simple enough to layer with longer chains."),
 ("fine-chain-necklace","Fine Chain Necklace","necklaces",4800,"925 sterling silver","silver","bar",2,
  "A delicate cable chain with a small bar charm. An everyday basic that works under a shirt collar or over a knit. Adjustable clasp fits 40 to 45 cm."),
 ("coin-drop-necklace","Coin Drop Necklace","necklaces",7400,"Gold-plated brass","gold","coin",6,
  "A round, lightly hammered coin hangs from a sturdy link chain. The hammered surface gives each piece its own pattern, so no two are exactly alike."),
 ("silver-hoop-earrings","Silver Hoop Earrings","earrings",3500,"925 sterling silver","silver","hoop",15,
  "Classic medium hoops with a hidden hinge clasp. Lightweight enough for all-day wear, with a smooth polished finish that works with both casual and dressed-up outfits."),
 ("pearl-stud-earrings","Pearl Stud Earrings","earrings",3200,"925 sterling silver, freshwater pearl","silver","stud",20,
  "Small freshwater pearl studs on sterling silver posts. A quiet pair that goes with almost everything and suits sensitive ears thanks to the silver backing."),
 ("drop-leaf-earrings","Drop Leaf Earrings","earrings",5200,"18k gold-plated sterling silver","gold","leaf",1,
  "A tiny leaf shape hangs from a short hook, moving gently as you walk. The gold plating is thick enough for regular wear when you take care of it."),
 ("beaded-chain-bracelet","Beaded Chain Bracelet","bracelets",4100,"925 sterling silver","silver","beads",9,
  "A slim bracelet of small silver beads on a flexible chain. Wear it on its own or with a watch. Fits wrists of 15 to 18 cm with an extender chain."),
 ("hammered-cuff-bracelet","Hammered Cuff Bracelet","bracelets",6200,"Gold-plated brass","gold","cuff",4,
  "An open cuff with a hand-hammered surface that slips on easily and can be gently adjusted for a snug fit. A bold piece that still feels light."),
 ("rope-link-bracelet","Rope Link Bracelet","bracelets",5900,"Rose gold-plated sterling silver","rose","rope",7,
  "Soft rose-toned links twisted into a rope pattern with a secure lobster clasp. Warm against the skin and easy to pair with silver or gold."),
]

def shape(cat, style, v):
    s = "url(#m)"
    if cat == "rings":
        out = f'<circle cx="400" cy="440" r="140" fill="none" stroke="{s}" stroke-width="{44 if style=="signet" else 30}"/>'
        if style == "signet":
            out += f'<ellipse cx="400" cy="298" rx="62" ry="48" fill="{s}"/>'
        if style == "twist":
            out += '<circle cx="400" cy="440" r="140" fill="none" stroke="#0003" stroke-width="30" stroke-dasharray="6 14"/>'
        if style == "stone":
            out += f'<circle cx="400" cy="296" r="38" fill="#EAF0F6" stroke="{s}" stroke-width="12"/>'
        return out
    if cat == "necklaces":
        out = f'<path d="M170 200 Q400 640 630 200" fill="none" stroke="{s}" stroke-width="7" stroke-dasharray="{14 if style!="coin" else 3} 5"/>'
        if style == "petal": out += f'<path d="M400 440 C340 490 360 560 400 590 C440 560 460 490 400 440Z" fill="{s}"/>'
        if style == "bar":   out += f'<rect x="360" y="455" width="80" height="14" rx="7" fill="{s}"/>'
        if style == "coin":  out += f'<circle cx="400" cy="490" r="52" fill="{s}"/><circle cx="400" cy="490" r="36" fill="none" stroke="#0002" stroke-width="3"/>'
        return out
    if cat == "earrings":
        out = ""
        for x in (290, 510):
            if style == "hoop":
                out += f'<circle cx="{x}" cy="420" r="95" fill="none" stroke="{s}" stroke-width="16"/>'
            elif style == "stud":
                out += f'<circle cx="{x}" cy="420" r="46" fill="#FBF8F3" stroke="#0001" stroke-width="3"/><circle cx="{x-12}" cy="408" r="12" fill="#fff"/>'
            else:
                out += f'<path d="M{x} 300 q22 0 22 24 v10" fill="none" stroke="{s}" stroke-width="8"/><path d="M{x+22} 340 C{x-20} 380 {x-10} 470 {x+22} 520 C{x+54} 470 {x+64} 380 {x+22} 340Z" fill="{s}"/>'
        return out
    if cat == "bracelets":
        if style == "beads":
            return f'<ellipse cx="400" cy="400" rx="210" ry="170" fill="none" stroke="{s}" stroke-width="26" stroke-linecap="round" stroke-dasharray="0 40"/>'
        if style == "cuff":
            return f'<path d="M210 330 A210 170 0 1 0 590 330" fill="none" stroke="{s}" stroke-width="42" stroke-linecap="round"/>'
        return (f'<ellipse cx="400" cy="400" rx="210" ry="170" fill="none" stroke="{s}" stroke-width="22"/>'
                '<ellipse cx="400" cy="400" rx="210" ry="170" fill="none" stroke="#0003" stroke-width="22" stroke-dasharray="4 16"/>')

def svg(cat, style, metal, v):
    a, b = METALS[metal]
    bg = "#FFFFFF" if v != 1 else "#F4EFE6"
    tf = {0: "", 1: "rotate(-12 400 400)", 2: "translate(400 400) scale(1.45) translate(-400 -400)"}[v]
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 800" width="800" height="800">'
            f'<defs><linearGradient id="m" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{a}"/><stop offset="1" stop-color="{b}"/></linearGradient></defs>'
            f'<rect width="800" height="800" fill="{bg}"/><circle cx="400" cy="400" r="330" fill="#EFE9DF" opacity="{0.55 if v==0 else 0.25}"/>'
            f'<g transform="{tf}">{shape(cat, style, v)}</g></svg>')

os.makedirs("public/images/products", exist_ok=True)
sql = ["-- Seed data. Run after schema.sql. Images are local SVGs in /public/images/products", "insert into public.products (slug, name, description, price, currency, category, material, images, stock, created_at) values"]
rows = []
for i, (slug, name, cat, price, mat, metal, style, stock, desc) in enumerate(P):
    imgs = []
    for v in range(3):
        path = f"/images/products/{slug}-{v+1}.svg"
        open("public" + path, "w").write(svg(cat, style, metal, v))
        imgs.append(path)
    arr = "array[" + ",".join(f"'{x}'" for x in imgs) + "]"
    rows.append(f"  ('{slug}', '{name}', '{desc}', {price}, 'KES', '{cat}', '{mat}', {arr}, {stock}, now() - interval '{i} hours')")
sql.append(",\n".join(rows) + ";")
open("supabase/seed.sql", "w").write("\n".join(sql) + "\n")

# Hero: a collage of all four categories
hero = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 800" width="800" height="800">'
        '<defs><linearGradient id="m" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F3D58B"/><stop offset="1" stop-color="#B8893B"/></linearGradient>'
        '<linearGradient id="s" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F7F7F7"/><stop offset="1" stop-color="#8F8F8F"/></linearGradient></defs>'
        '<rect width="800" height="800" fill="#EFE9DF"/><circle cx="560" cy="250" r="230" fill="#F1E3C6"/>'
        '<circle cx="270" cy="560" r="130" fill="none" stroke="url(#m)" stroke-width="34"/>'
        '<ellipse cx="270" cy="440" rx="50" ry="40" fill="url(#m)"/>'
        '<circle cx="560" cy="250" r="110" fill="none" stroke="url(#s)" stroke-width="18"/>'
        '<path d="M120 120 Q330 420 560 120" fill="none" stroke="url(#s)" stroke-width="6" stroke-dasharray="12 5"/>'
        '<circle cx="340" cy="290" r="34" fill="url(#m)"/>'
        '<ellipse cx="560" cy="600" rx="150" ry="110" fill="none" stroke="url(#s)" stroke-width="22" stroke-linecap="round" stroke-dasharray="0 34"/></svg>')
open("public/images/hero.svg", "w").write(hero)
print("generated", len(P), "products")
