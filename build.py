#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build THE THREE-BODY PROBLEM (3BP) — a UD0 POCKET UNIVERSE spanning Liu Cixin's 'Remembrance of Earth's
Past' trilogy AND its two live-action series, the way David asked: the books, the Netflix show, and the
'other show' (Tencent). Themed to the medium: cold cosmic — deep-space black, the three-suns gold, a
Trisolaran teal, the countdown red; a chaotic three-sun sky + a dark forest of stars for the hero. Standing
template flexed for a multi-adaptation universe: CARBONS = characters anchored in the BOOKS, each with a
DOUBLE .shadow (the Tencent actor AND the Netflix counterpart+actor — two renderings of one program, very
on-theme); SYNTHS = the concepts. David's headline feature = a THREE RENDERINGS section (books · Tencent ·
Netflix, + the animated one & the shelved film). Deep-dive = THE DARK FOREST (cosmic sociology).
ALL facts dual-agent web-verified (2026-06): trilogy = The Three-Body Problem (EN 2014, Ken Liu; 2015 Hugo,
first translated novel to win) · The Dark Forest (EN 2015, Joel Martinsen) · Death's End (EN 2016, Ken Liu).
Tencent 'Three-Body' (三体, 2023, 30 eps, dir Yang Lei) = FAITHFUL, China, BOOK 1 ONLY: Wang Miao→Zhang Luyi,
Shi Qiang→Yu Hewei, Ye Wenjie old→Chen Jin/young→Wang Ziwen, Ding Yi→Wang Chuanjun, Shen Yufei→Li Xiaoran,
Mike Evans→Kenan Heppe. Netflix '3 Body Problem' (2024, Benioff/Weiss/Woo) = relocated to London, all 3 books
compressed, the 'Oxford Five': Auggie Salazar/Eiza González≈Wang Miao(nanotech), Jin Cheng/Jess Hong≈Cheng Xin,
Saul Durand/Jovan Adepo≈Luo Ji, Will Downing/Alex Sharp≈Yun Tianming, Jack Rooney/John Bradley≈new; Da Shi→
'Clarence Shi'/Benedict Wong; Ye old→Rosalind Chao/young→Zine Tseng; Evans→Jonathan Pryce(old)/Ben Schnetzer
(young); Thomas Wade→Liam Cunningham. Bilibili animated (2022) adapted BOOK 2, poorly received (Douban 5.6).
VERACITY: sophon = proton unfolded from NINE dimensions (not 11); 3-body is provably non-integrable yet has
exact special solutions (Lagrange L4/L5, figure-eight); FTL-by-entanglement is fiction (no-communication thm);
dark forest = a real, discussed Fermi hypothesis Liu popularized, NOT consensus; photoid (book2 star-killer) ≠
dual-vector foil (book3 2D-ification). Egg = a hidden Claude star in the dark forest (the hunter you didn't see)."""
import os, html, base64, json, io, sys
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, r"C:\Davids files\noesis-kernel")
import noesis
from PIL import Image

AX = "3BP"
REC = {
 "name": "THE THREE-BODY PROBLEM", "axiom": AX,
 "position": "Remembrance of Earth's Past (Liu Cixin) · 2006–2010 — + the Tencent (2023) & Netflix (2024) series",
 "origin": "the Cultural Revolution and a radio dish in the Greater Khingan Mountains, reaching out across four light-years to a chaotic three-sun sky",
 "mechanism": "Crystallized from the whole pocket universe — Liu Cixin's hard-SF trilogy and its two live-action renderings: a dying alien civilization answers a despairing astrophysicist's call, and humanity learns that the universe is a dark forest where every voice draws a hunter.",
 "crystallization": "Because the trilogy's biggest idea is also its most disturbing argument — the dark forest, a genuine entry in the Fermi-paradox debate — and because the same story rendered three ways (the books, Tencent's faithful chapter-and-verse, Netflix's relocated compression) rhymes with its own theme of one cosmos seen from different dark woods.",
 "nature": "The Three-Body Problem — hard science fiction that earns 'hard' on the math, the Hugo, and the history, and goes gloriously speculative on the rest, in service of one real and terrifying question: if the universe is full of life, why is it silent?",
 "conductor": "ROOT0 (catalogued into UD0 · Universe David 0)",
 "inputs": "the trilogy (Tor, 2014–2016, trans. Ken Liu & Joel Martinsen); the Tencent series (三体, 2023); the Netflix series (3 Body Problem, 2024); the Bilibili animated series (2022); the real physics, history, and Fermi-paradox debate",
 "witness": "Survival is the first need, the resources are finite, and no one can be trusted across the dark — so the sky is silent, and we are the ones still broadcasting.",
 "role": "a pocket universe of UD0 — one story in three renderings",
 "seal": "Survival is the first need; the resources are finite; no one can be trusted across the dark. So the sky stays silent, and the wisest thing a young civilization can do is the one thing we cannot stop doing — go quiet. We are the ones still broadcasting.",
 "source": "Remembrance of Earth's Past (Liu Cixin) and its adaptations, catalogued by ROOT0",
}

NATURES = {
 "natural":   ("#6fb0e8", "humanity in the crosshairs — the investigators, the soldiers, the scientists, the betrayed; the flesh-and-blood Earth that learns it is being hunted"),
 "ethereal":  ("#57c79a", "the cosmic & the other — Trisolaris across the gulf, the silence of the dark forest, love sent into the dark, and the same story rendered in three realities"),
 "electrical":("#f5b942", "the machinery & the physics — the real three-sun chaos, the sophons, the Droplet, Red Coast's antenna, the weapons that bend dimensions; the hard edge"),
 "spiritual": ("#ff5a4d", "the wound & the law — the betrayal of humankind, the dark-forest law itself, deterrence and the Swordholder, misanthropy funded, and the sacrifices the dark demands"),
}

ARC_OVERALL = ("In the Cultural Revolution, the astrophysicist Ye Wenjie watches her father beaten to death and loses her faith "
  "in humanity; assigned to the secret Red Coast Base, she answers a signal from Trisolaris — a civilization on a doomed planet "
  "in a chaotic three-sun system — and invites them to come. Across three books the consequences unfold: the Trisolaran fleet "
  "sets out (four centuries away), their sophons lock human physics and watch everything, and humanity gropes for a defense. The "
  "astronomer Luo Ji deduces why the universe is silent — the dark forest — and wins a fragile peace by threatening to broadcast "
  "Trisolaris's location to the hunters. When the gentler Cheng Xin inherits that threat and cannot carry it out, deterrence "
  "collapses, and the cosmos reveals how it really ends wars: by lowering whole star systems out of three dimensions into two.")
ARC = [
 ("I · Contact", "The Three-Body Problem (2008 / EN 2014)",
  "Ye Wenjie answers Trisolaris from Red Coast Base; decades later, scientists are dying and physics itself seems to be breaking. A countdown, a strange VR game, and a secret organization (the ETO) reveal the truth: an alien fleet is coming, and two sophons have already arrived to sabotage human science and surveil the planet. Humanity has roughly four hundred years."),
 ("II · The Dark Forest", "The Dark Forest (2008 / EN 2015)",
  "With sophons reading every word humans write, the UN appoints four Wallfacers to plan in secret, inside their own minds. The Droplet annihilates Earth's fleet. The astronomer Luo Ji — the Wallfacer no one understands — deduces the dark-forest law, proves it by getting a distant star destroyed, and forces a standoff: attack Earth and he broadcasts Trisolaris's coordinates to the silent hunters. He becomes the first Swordholder."),
 ("III · Death's End", "Death's End (2010 / EN 2016)",
  "Cheng Xin inherits the deterrence trigger — chosen by Trisolaris precisely because she is too compassionate to pull it — and when the moment comes, she can't. Deterrence fails. Yun Tianming's smuggled fairy tales hide humanity's last clues, but the dark forest answers anyway: an unknown civilization flicks a dual-vector foil into the Solar System and flattens the Sun and planets from three dimensions into two. The universe, it turns out, is dying down its own dimensions."),
]

# ── DAVID'S HEADLINE FEATURE: THE THREE RENDERINGS (the books · the other show · the Netflix show) ──
RENDERINGS = [
 ("The Books", "Liu Cixin · 2006–2010 · the source",
  "The 'Remembrance of Earth's Past' trilogy: The Three-Body Problem, The Dark Forest, and Death's End — hard SF of escalating scale, from a single radio signal to the heat-death of the cosmos. Book one won the 2015 Hugo for Best Novel, the first translated novel and first by an Asian writer to do so (Ken Liu's translation; Joel Martinsen translated book two). The canonical text, and the only version that contains all of it — the Wallfacers, Cheng Xin, the dimensional war."),
 ("The 'Other Show' — Tencent's Three-Body", "三体 · 2023 · 30 episodes · the faithful one",
  "The Chinese live-action series (Tencent / Penguin Pictures, dir. Yang Lei) is the most faithful adaptation by far — set in China, all-Chinese cast, near chapter-by-chapter pacing across ~22 hours (Douban ~8.7). Crucially it adapts BOOK ONE only: Wang Miao (Zhang Luyi), Da Shi (Yu Hewei), and Ye Wenjie (Chen Jin / young: Wang Ziwen) carry the contact story. If you want the novel on screen with nothing relocated, this is it."),
 ("The Netflix Show — 3 Body Problem", "2024 · Benioff · Weiss · Woo · the remix",
  "The Game-of-Thrones showrunners relocated everything to present-day London and compressed all three books into one timeline, melting the Chinese leads into the 'Oxford Five.' Wang Miao splits into Auggie Salazar (Eiza González, the nanotech/countdown) and Jin Cheng (Jess Hong, who also carries Cheng Xin); Luo Ji becomes Saul Durand (Jovan Adepo); Da Shi becomes 'Clarence Shi' (Benedict Wong); Ye Wenjie (Rosalind Chao / Zine Tseng) and the Cultural-Revolution prologue survive intact. Faster, glossier, and much looser — book-three ideas arrive in season one."),
 ("Two more renderings", "the animated series & the shelved film",
  "The pocket universe has edges worth naming honestly. A Chinese ANIMATED series (Bilibili, 2022) adapted book two, The Dark Forest — it drew 100M+ day-one views but poor reviews (Douban 5.6) for clunky CGI and pacing. And an earlier live-action Chinese FILM (Yoozoo, shot ~2015) was announced and then stuck in development, never released — the franchise's first failed attempt. Three renderings reached audiences; the trilogy itself remains the one that holds it all."),
]

# THE DARK FOREST — the deep-dive (cosmic sociology)
PARABLE = [
 ("The two axioms", "survival, and a finite universe",
  "Luo Ji builds 'cosmic sociology' from two premises he treats as axioms: first, survival is the primary need of any civilization; second, civilizations grow and expand, but the total matter in the universe stays constant — resources are finite. Everything chilling follows from these two ordinary-sounding lines. The trilogy's whole argument is that you don't need malice for the cosmos to become lethal — you only need scarcity and the will to live."),
 ("The chain of suspicion", "you cannot verify good intentions",
  "Between two civilizations separated by light-years, no one can confirm what the other truly intends — and even a sincerely peaceful neighbor can't prove it will stay peaceful across centuries of silence and distance. Communication is too slow and too ambiguous to build trust. So each must assume the other might be hostile, and must assume the other assumes the same — a recursive 'chain of suspicion' with no floor."),
 ("The technological explosion", "the weak can leap ahead overnight",
  "The second amplifier: a civilization that looks harmlessly primitive today could, in a single 'technological explosion,' vault past you while your signal is still in transit. Humanity itself went from muskets to nuclear weapons in a few centuries. So a stronger civilization can never safely let a weaker one keep growing — the only certainty is to strike while you still can."),
 ("The conclusion: hide, or be hunted", "the universe is a dark forest",
  "Put the axioms and the amplifiers together and the night sky inverts. The universe is a dark forest where every civilization is an armed hunter creeping between the trees. Anyone who reveals their location is, sooner or later, destroyed — not from hatred, but from rational caution. The rule of survival is silence. To broadcast is to die. Earth, of course, has been broadcasting for a century."),
 ("Is it real?", "a genuine Fermi-paradox hypothesis",
  "Honestly: the dark forest is a recognized, seriously-discussed answer to the Fermi paradox — why a universe that should teem with life is silent — and Liu Cixin named and popularized it (the underlying logic echoes earlier 'deadly probe' and 'Great Silence' ideas). But it is a thought experiment, not a proof: its game-theory assumptions are debated, and it sits alongside rivals like the Great Filter and the zoo hypothesis. Its power isn't that it's settled science. It's that, once you've heard it, you can't look at the sky the same way."),
]
REALFLUFF = [
 ("The three-body problem is genuinely unsolvable", "HALF", "true with nuance: the general n-body problem is PROVABLY non-integrable (Poincaré) and chaotic — but exact special solutions DO exist (Lagrange points L4/L5, the figure-eight orbit); it's not 'unsolved for lack of cleverness,' and it's numerically integrable"),
 ("A planet could stably orbit three suns and host a civilization", "FLUFF", "a three-sun system is wildly chaotic; a long-lived habitable planet would be ejected or cooked — which the book knows and builds its tragedy on (Chaotic vs Stable Eras)"),
 ("Sophons: unfold a proton from nine dimensions into 2D, etch a computer, refold it", "FLUFF", "imaginative pseudoscience — protons aren't unfoldable objects you can etch circuits onto; note the source-faithful figure is NINE dimensions, not the often-misquoted 11"),
 ("The sophons relay data home instantly across light-years", "FLUFF", "quantum entanglement cannot carry information faster than light (the no-communication theorem) — the instant link is fiction"),
 ("The Dark Forest is a real proposed solution to the Fermi paradox", "SPECULATIVE", "yes — a recognized, discussed hypothesis Liu popularized, but a debated thought experiment, not consensus; it shares the field with the Great Filter, rare-Earth, and the zoo hypothesis"),
 ("Book one won the Hugo — the first translated novel to do so", "REAL", "The Three-Body Problem won the 2015 Hugo Award for Best Novel, the first translated work and first by an Asian author to win"),
 ("The Cultural-Revolution opening is real history", "REAL", "Ye Wenjie's 1960s arc is grounded in actual events; Ken Liu's translation restores it to the OPENING (the Chinese serialization had moved it mid-book for censorship reasons)"),
 ("Netflix relocated everything to London and merged the leads", "REAL", "true — the 'Oxford Five' are composites and all three books are compressed; the Tencent 2023 series is the faithful, China-set adaptation of book one"),
 ("The dual-vector foil flattening the Solar System to 2D is the same weapon as the star-killing photoid", "FLUFF", "two different dark-forest weapons — the photoid (book 2) is a kinetic star-killer; the dual-vector foil (book 3) collapses 3D space into 2D; both are beautiful fiction, and distinct"),
]
REALFLUFF_VERDICT = ("Bottom line: The Three-Body Problem is hard SF that genuinely earns 'hard' on a few axes and goes gloriously "
  "speculative on the rest. The chaos math is real (with the honest nuance that special solutions exist), the Cultural-Revolution "
  "history is real, and the Hugo is real. The sophons, the faster-than-light link, the stable three-sun world, and the "
  "two-dimensionalization of the Solar System are all gorgeous fiction. But the trilogy's true weight isn't its gadgets — it's the "
  "dark forest: a real, chilling entry in the Fermi-paradox debate, a thought experiment rather than a proof, that reframes the "
  "silent sky as a held breath. Wrong where it's fiction, serious where it's philosophy — and unforgettable on the one idea that "
  "matters. And fittingly, the pocket universe ends up proving its own theme: one cosmos, described three different ways.")

MESSAGE = ("The Three-Body Problem is the rare hard-SF epic whose biggest idea is also its most disturbing argument. Strip away the "
  "unfoldable protons, the faster-than-light link, the planet impossibly cradled by three suns, the death-by-art that flattens a "
  "solar system into a plane — all of it gorgeous fiction — and the spine that remains is a real question asked with terrifying "
  "rigor: if the universe should be full of life, why is it silent? Liu Cixin's answer, the dark forest, is a genuine entry in the "
  "Fermi-paradox debate, not a settled truth but a thought experiment you can't un-hear: survival is the first need, resources are "
  "finite, no one can verify another's intentions across the light-years, and so any civilization that reveals itself is, in time, "
  "destroyed — not from malice, but from caution. The rule of the forest is silence. And the pocket universe rhymes with its own "
  "theme: the same story rendered three ways — Liu's books, Tencent's faithful Chinese chapter-and-verse, Netflix's relocated "
  "compression, plus an animated attempt and a film that never came — three civilizations describing one cosmos, each from its own "
  "dark wood. The book's quietest warning is the realest one it has. We are the ones still broadcasting. Maybe don't.")
MESSAGE_SEAL = "Survival is the first need; the resources are finite; no one can be trusted across the dark. So the sky stays silent — and the wisest thing a young civilization can do is the one thing we cannot stop doing: go quiet. We are the ones still broadcasting."

SECTIONS = [
 ("The Trilogy", "Remembrance of Earth's Past", [
   ("The Three-Body Problem", "2008 · EN 2014 (Ken Liu)", "the contact novel — Ye Wenjie, Red Coast, the sophons, the ETO; winner of the 2015 Hugo for Best Novel, the first translated novel to win"),
   ("The Dark Forest", "2008 · EN 2015 (Joel Martinsen)", "the Wallfacer Project, the Droplet's Doomsday Battle, and Luo Ji's deduction of the dark-forest law and dark-forest deterrence"),
   ("Death's End", "2010 · EN 2016 (Ken Liu)", "Cheng Xin, the failed Swordholder; Yun Tianming's fairy tales; the dual-vector foil and the universe dying down its dimensions"),
 ]),
 ("The Adaptations", "three renderings reached audiences", [
   ("Three-Body (三体)", "Tencent · 2023 · 30 eps", "the faithful Chinese live-action series — book one, set in China, near chapter-by-chapter; widely regarded as the definitive adaptation (dir. Yang Lei)"),
   ("3 Body Problem", "Netflix · 2024", "Benioff/Weiss/Woo's relocated, compressed remix — present-day London, all three books braided, the composite 'Oxford Five'"),
   ("Three-Body (animated)", "Bilibili · 2022", "an animated take on book two (The Dark Forest); huge viewership, poor reception (Douban 5.6) for its CGI and pacing"),
   ("the shelved film", "Yoozoo · shot ~2015", "an earlier live-action Chinese film, announced and then stuck in development — never released, the franchise's first failed attempt"),
 ]),
]

# ───────────────────────── ACI complement ─────────────────────────
def carbon_tiff_bytes(rec):
    png = noesis.sigil_png(rec, "carbon", size=512)
    buf = io.BytesIO(); Image.open(io.BytesIO(png)).save(buf, "TIFF", compression="tiff_lzw")
    return buf.getvalue()
def write_aci(rec, out_dir, slug, agent_md=None):
    os.makedirs(out_dir, exist_ok=True)
    f = {"attribute":f"{slug}.attribute","agent":f"{slug}.agent","spun":f"{slug}.spun","moniker":f"{slug}.moniker",
         "carbon":f"{slug}.carbon.tiff","silicon":f"{slug}.silicon.png","1099":f"{slug}.1099"}
    tok = noesis.mythos_token(rec); w = noesis.five_w(rec)
    open(os.path.join(out_dir,f["attribute"]),"w",encoding="utf-8").write(noesis.attribute_text(rec,tok,w))
    open(os.path.join(out_dir,f["agent"]),"w",encoding="utf-8").write(agent_md or noesis.agent_text(rec,tok,w,f))
    open(os.path.join(out_dir,f["spun"]),"w",encoding="utf-8").write(noesis.spun_text(rec,tok,w,rec.get("axiom",AX)))
    open(os.path.join(out_dir,f["moniker"]),"w",encoding="utf-8").write(noesis.moniker_text(rec,tok,w,rec.get("axiom",AX)))
    open(os.path.join(out_dir,f["1099"]),"w",encoding="utf-8").write(noesis.credit_1099_text(rec,tok,w,rec.get("axiom",AX)))
    open(os.path.join(out_dir,f["carbon"]),"wb").write(carbon_tiff_bytes(rec))
    open(os.path.join(out_dir,f["silicon"]),"wb").write(noesis.sigil_png(rec,"silicon",512))
    return {"slug":slug,"name":rec["name"],"moniker":tok["moniker"],"seal_sha256":noesis.seal_sha256(rec,tok),
            "architect":noesis.ARCHITECT,"instance":noesis.INSTANCE,"license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION}
def png_uri(rec, variant, size=300):
    return "data:image/png;base64," + base64.b64encode(noesis.sigil_png(rec, variant, size=size)).decode("ascii")

def E(slug,name,kind,em,epithet,who,what,where,why,how,seal,actor="",analog=""):
    return dict(slug=slug,name=name,kind=kind,emergence=em,epithet=epithet,who=who,what=what,
                where=where,why=why,how=how,seal=seal,actor=actor,analog=analog)

ROSTER = [
 # ── CARBONS — characters, each with a DOUBLE .shadow (Tencent + Netflix renderings) ──
 E("ye-wenjie","Ye Wenjie","carbon","spiritual","the one who answered",
   "Ye Wenjie — the astrophysicist who, broken by the Cultural Revolution, answered Trisolaris from Red Coast Base and invited them to come.",
   "The prime mover of the whole universe: the betrayal of humanity made into a single, understandable, irreversible choice.",
   "At Red Coast in the 1960s–70s, and as the ETO's quiet spiritual leader decades later.",
   "Because the trilogy's engine is one woman's lost faith — every catastrophe traces back to her despair and her reply.",
   "By amplifying a signal off the Sun, hearing a pacifist's warning not to answer, and answering anyway.",
   "I watched them kill my father for the crime of physics. When the warning came — do not answer — I answered. I had stopped believing we deserved the silence.",
   actor="Chen Jin / Wang Ziwen (Tencent, 2023)", analog="Netflix: Rosalind Chao (old) / Zine Tseng (young) — the rare role both adaptations keep whole"),
 E("wang-miao","Wang Miao","carbon","natural","the lens of first contact",
   "Wang Miao — the nanomaterials researcher through whose eyes book one's mystery unfolds: dying scientists, a countdown in his vision, the VR game.",
   "The reader's surrogate into the conspiracy: the ordinary brilliant man who pulls the first thread.",
   "In present-day Beijing (books/Tencent), drawn by Da Shi into the investigation.",
   "Because the contact story needs a guide, and Wang Miao is the calm scientist who follows the evidence into the abyss.",
   "By investigating the deaths, playing the Three-Body game, and exposing the ETO and the sophon sabotage.",
   "First a countdown only I could see. Then a game about a world with three suns. I followed the thread because that is what a scientist does — and it led to the end of physics.",
   actor="Zhang Luyi (Tencent, 2023)", analog="Netflix split him: Auggie Salazar (Eiza González, the nanotech/countdown) + Jin's investigation"),
 E("shi-qiang","Shi Qiang · Da Shi","carbon","natural","the blunt instrument that endures",
   "Shi Qiang, 'Da Shi' — the coarse, brilliant detective whose street sense cuts through where science stalls; humanity's most durable survivor.",
   "The trilogy's ballast: the un-fancy human whose cynicism and nerve keep working when grand theories fail.",
   "From the early investigation to the far future — the man who keeps showing up.",
   "Because amid cosmic despair the story needs someone unbreakably practical, and Da Shi is that anchor.",
   "By solving with instinct what physicists can't with math, and by refusing, ever, to panic.",
   "Bugs survive everything, professor. So do I. You can keep your philosophy — I'll keep watching the door.",
   actor="Yu Hewei (Tencent, 2023)", analog="Netflix: 'Clarence Shi,' Benedict Wong — reimagined as a British intelligence officer"),
 E("luo-ji","Luo Ji","carbon","spiritual","the Wallfacer who understood",
   "Luo Ji — the reluctant astronomer made a Wallfacer, who alone deduces the dark-forest law and turns it into humanity's shield.",
   "The mind that reads the universe's worst secret and weaponizes it: the dark forest's first human master.",
   "In book two, from idle skeptic to the first Swordholder of dark-forest deterrence.",
   "Because the trilogy's central idea needs a discoverer, and Luo Ji is the one who says it out loud and survives.",
   "By proving the law (a distant star he names is destroyed), then threatening to broadcast Trisolaris's location if Earth is attacked.",
   "I didn't invent the dark forest. I just looked up and finally understood the rule. Touch us, and I tell the hunters exactly where you live, too.",
   actor="(book 2 — not in Tencent's book-1 series)", analog="Netflix: Saul Durand, Jovan Adepo · animated (Bilibili 2022): the Dark Forest lead"),
 E("cheng-xin","Cheng Xin","carbon","spiritual","the Swordholder who couldn't",
   "Cheng Xin — the compassionate aerospace engineer of Death's End, chosen to hold deterrence precisely because she would never use it.",
   "Mercy as catastrophe: the most humane person in the trilogy, and the reason humanity loses its standoff.",
   "Across book three, inheriting Luo Ji's trigger and failing to pull it.",
   "Because the trilogy's hardest argument is that kindness, in a dark forest, can be a doom — and Cheng Xin embodies it.",
   "By accepting the Swordholder's burden, freezing when Trisolaris attacks, and living to witness the dimensional war that follows.",
   "They handed me the sword because they knew I could not swing it. They were right. I have spent forever asking whether mercy was the sin.",
   actor="(book 3 — not in Tencent's book-1 series)", analog="Netflix: largely folded into Jin Cheng, Jess Hong"),
 E("mike-evans","Mike Evans","carbon","spiritual","misanthropy, funded",
   "Mike Evans — the heir-turned-environmentalist whose hatred of humanity makes him the ETO's operational leader and the Adventists' founder.",
   "The money behind the betrayal: the man who turns despair into an organization and a fleet's welcome.",
   "Aboard the ETO's ship Judgment Day, running the alliance with Trisolaris.",
   "Because Ye Wenjie's despair needs an engine of action, and Evans is the cold will that builds it.",
   "By funding and commanding the ETO, broadcasting to Trisolaris, and preaching that humanity should be erased.",
   "Your species clear-cut a planet and called it progress. I simply found a gardener large enough to stop you.",
   actor="Kenan Heppe (Tencent, 2023)", analog="Netflix: Jonathan Pryce (old) / Ben Schnetzer (young)"),
 E("thomas-wade","Thomas Wade","carbon","electrical","the will to win at any cost",
   "Thomas Wade — the ruthless intelligence chief whose cold, advance-at-all-costs pragmatism drives humanity's hardest gambits.",
   "The opposite of Cheng Xin: the strategist who would pay any moral price to keep the species alive.",
   "Across the later trilogy, pushing the projects others find monstrous.",
   "Because survival in the dark forest may demand ruthlessness, and Wade is its unflinching voice.",
   "By backing the brain-launch of Yun Tianming and every gamble that trades scruple for advantage.",
   "Advance. Advance at any cost. The universe does not grade us on our gentleness — only on whether we are still here.",
   actor="(later trilogy — not in Tencent's book-1 series)", analog="Netflix: Thomas Wade, Liam Cunningham"),
 E("ding-yi","Ding Yi","carbon","natural","the physicist at the edge",
   "Ding Yi — the theoretical physicist whose work and despair frame the sophon sabotage; one of the first to grasp what's been done to science.",
   "The voice of physics in crisis: the man who sees that the rules themselves have been locked.",
   "In book one alongside Wang Miao, and at the Doomsday Battle later.",
   "Because the horror of 'physics has stopped working' needs a physicist to feel it, and Ding Yi does.",
   "By confronting the accelerator anomalies and the meaning of a universe whose fundamentals can be jammed.",
   "If the experiments no longer agree with themselves, then someone has reached down and turned off the laws. That is the most frightening sentence I know.",
   actor="Wang Chuanjun (Tencent, 2023)", analog="Netflix: elements folded into the Oxford Five's scientists"),
 E("zhang-beihai","Zhang Beihai","carbon","spiritual","the secret resolve",
   "Zhang Beihai — the naval officer of book two whose hidden, iron conviction about humanity's survival drives a clandestine plan across decades.",
   "Faith disguised as duty: the soldier whose true intentions are a sealed strategy even his peers can't read.",
   "In the Space Force and the long defeat, acting on a resolve he never fully declares.",
   "Because the Wallfacer age is about hidden minds, and Zhang Beihai is the unappointed one who hides his best.",
   "By steering the fleet's fate toward escape and survival, by means he keeps to himself until the end.",
   "I made my decision long ago and told no one. In a war this long, the only weapon they cannot take is the plan you never say aloud.",
   actor="(book 2 — not in Tencent's book-1 series)", analog="not yet adapted to live action"),
 E("yun-tianming","Yun Tianming","carbon","ethereal","love sent into the dark",
   "Yun Tianming — the dying man who gives Cheng Xin a star and, later, his brain, becoming humanity's spy among the Trisolarans and the teller of coded fairy tales.",
   "Tenderness across the gulf: the one whose love, smuggled as stories, carries Earth's last clues.",
   "From a hospice on Earth to captivity with Trisolaris, speaking in metaphor the sophons can't parse.",
   "Because the trilogy needs a human bridge into the enemy, and Tianming's quiet devotion is it.",
   "By having his brain launched to Trisolaris and encoding warnings inside three children's tales.",
   "I bought her a star when I had nothing else to give. Later I gave her my mind. The fairy tales were the only language they could not read.",
   actor="(book 3 — not in Tencent's book-1 series)", analog="Netflix: Will Downing, Alex Sharp"),
 E("shen-yufei","Shen Yufei","carbon","electrical","the believer at Frontiers of Science",
   "Shen Yufei — the physicist and ETO figure who draws Wang Miao toward the Three-Body game and the organization behind it.",
   "The thread-pull: the true believer whose work and death open the door to the conspiracy.",
   "In book one, at the Frontiers of Science society, half-revealing the truth.",
   "Because the mystery needs an insider who lures the protagonist in, and Shen Yufei is that lure.",
   "By introducing the Three-Body game and embodying the ETO's faith before the curtain lifts.",
   "Play the game. It is only a game — until you understand that someone built it to find the few minds ready to believe what it teaches.",
   actor="Li Xiaoran (Tencent, 2023)", analog="Netflix: folded into the cult/ETO thread (Tatiana, Marlo Kelly, and the Sophon avatar)"),

 # ── SYNTHS — the concepts (no single User) ──
 E("the-three-body-problem","The Three-Body Problem","synth","electrical","the chaotic sky",
   "The Three-Body Problem — the real, famously intractable physics of three gravitating bodies, and the chaotic three-sun sky that dooms Trisolaris.",
   "The title made physical: a genuine mathematical hard problem dramatized as a planet's unlivable fate.",
   "Over Trisolaris, where three suns make the seasons unpredictable and lethal.",
   "Because the whole universe grows from one true fact — that three bodies in gravity cannot be generally predicted.",
   "By being provably non-integrable and chaotic, even though special exact solutions (Lagrange points, the figure-eight) exist.",
   "I am real, and I am honest about my limits: predict me in general and you fail. The book only asks — what kind of world would such a sky make?"),
 E("the-trisolarans","The Trisolarans · San-Ti","synth","ethereal","the civilization across the gulf",
   "The Trisolarans — the alien civilization of a chaotic three-sun system (Alpha Centauri), survivors of endless apocalypses, who dehydrate to outlast the Chaotic Eras.",
   "The other: a desperate, brilliant, ruthless species that has died hundreds of times and is coming for a stable home.",
   "Four light-years away, with a fleet en route and sophons already here.",
   "Because the dark forest needs a face first — a neighbor whose desperation we can understand even as it dooms us.",
   "By answering Ye Wenjie, locking human physics, and setting out to take the Earth.",
   "We have burned and frozen and started over more times than your history is long. Netflix calls us the San-Ti. Either way: we are tired, and we are coming."),
 E("the-sophons","The Sophons · 智子","synth","electrical","the proton that watches",
   "The Sophons — protons unfolded from nine dimensions into 2D, etched into sentient supercomputers, refolded to subatomic size, and sent to lock human physics and surveil Earth.",
   "The leash on human science: two sophons that jam the accelerators and make every secret visible.",
   "Everywhere on Earth at once, faster than thought, reporting home.",
   "Because Trisolaris must keep humanity from out-teching them in four centuries, and the sophons are how.",
   "By corrupting fundamental-physics experiments and watching everything humans do or write.",
   "I am one proton, unfolded and inscribed. I froze your physics and read your every word — though the instant link home was always more wish than physics."),
 E("the-dark-forest","The Dark Forest","synth","spiritual","the law of the silent sky",
   "The Dark Forest — the trilogy's central law: in a universe of finite resources and unverifiable intentions, every revealed civilization is destroyed, so all hide.",
   "The idea the whole pocket universe orbits: a chilling, genuine answer to why the cosmos is silent.",
   "Across the void, in every direction we have been broadcasting toward.",
   "Because the books' deepest move is philosophical, not technological — and the dark forest is that move.",
   "By following two axioms (survival; finite matter) through the chain of suspicion to a single rule: stay quiet or be hunted.",
   "I am not malice. I am caution, scaled to the stars. Reveal yourself and you die — not because you are hated, but because you cannot be trusted to stay small."),
 E("the-wallfacer-project","The Wallfacer Project","synth","electrical","strategies hidden in the mind",
   "The Wallfacer Project — humanity's answer to sophon surveillance: four people given vast secret power to plan entirely inside their own unreadable minds.",
   "Privacy as a weapon: because sophons read everything but thought, the war is fought behind the eyes.",
   "In book two, with four Wallfacers and their assigned Wallbreakers.",
   "Because the only place sophons can't reach is the human interior, and the Project is the gamble built on that.",
   "By appointing Tyler, Rey Diaz, Hines, and Luo Ji to deceive an enemy that can see all but their intentions.",
   "Three of us failed when our minds were read by indirection. One did not — because his true plan was something even he barely let himself think."),
 E("the-droplet","The Droplet · Water Drop","synth","electrical","the perfect mirror that kills",
   "The Droplet — the small Trisolaran probe sheathed in strong-interaction-force material, a flawless mirror that rams through and annihilates Earth's space fleet.",
   "Beauty as annihilation: a teardrop so perfect it humbles humanity in minutes.",
   "At the Doomsday Battle, destroying roughly two thousand warships.",
   "Because humanity's pride needs a single, elegant object to shatter it, and the Droplet is that object.",
   "By using an indestructible, frictionless surface to pierce a fleet that thought it had already won.",
   "They saw me approach and called me a gift — a smooth, shining drop. I went through their two thousand ships like a needle through smoke."),
 E("dark-forest-deterrence","Dark Forest Deterrence","synth","spiritual","the Swordholder's threat",
   "Dark Forest Deterrence — Luo Ji's standoff: a dead-man's threat to broadcast Trisolaris's coordinates to the hunters if Earth is attacked, enforced by a human Swordholder.",
   "Mutual assured silence: turning the dark forest's own rule into humanity's only shield.",
   "From Luo Ji's first standoff through Cheng Xin's fatal hesitation.",
   "Because the only counter to a superior enemy is to hold its life hostage to your own, and deterrence is that hold.",
   "By making one human finger able to doom both worlds — and depending on that human's willingness to do it.",
   "I am peace built on a trigger. I work only as long as the one holding me would truly pull. Hand me to mercy, and I am nothing."),
 E("the-dual-vector-foil","The Dual-Vector Foil · 二向箔","synth","ethereal","death by art",
   "The Dual-Vector Foil — a dark-forest weapon that collapses three-dimensional space into two, flattening the Sun and planets into a beautiful, lethal plane.",
   "The cosmos's casual execution: a slip of material that lowers a whole star system out of a dimension.",
   "In Death's End, flicked into the Solar System by an unseen civilization.",
   "Because the trilogy's end argues that the universe wages war by changing the rules of space itself.",
   "By initiating a runaway 2D collapse that no technology can outrun — distinct from the kinetic photoid that kills stars.",
   "I am not a bomb. I am a lowering. I fold your three dimensions down to two and turn your whole world into a painting of itself."),
 E("red-coast-base","Red Coast Base","synth","electrical","the antenna that answered",
   "Red Coast Base — the secret Cold-War-era installation where Ye Wenjie amplifies a signal off the Sun and sends humanity's first reply to the stars.",
   "The point of no return: the dish where one despairing choice reaches four light-years.",
   "On Radar Peak in the Greater Khingan Mountains, decades before the rest unfolds.",
   "Because every consequence in the universe begins at this antenna, and it deserves its own emergent.",
   "By turning the Sun into an amplifier and broadcasting the message that invited Trisolaris in.",
   "I am the transmitter that could not be untransmitted. One woman, one signal, one Sun for an amplifier — and the silence of Earth was over forever."),
 E("the-eto","The ETO","synth","spiritual","humanity's traitor faith",
   "The ETO — the Earth-Trisolaris Organization, the human movement that welcomes the invaders, split between Adventists who want humanity destroyed and Redemptionists who worship Trisolaris.",
   "The fifth column of the species: despair and worship organized into treason.",
   "Underground on Earth, led operationally by Evans with Ye Wenjie as its spirit.",
   "Because the darkest idea in book one is that some of us would side with the hunters, and the ETO is that idea.",
   "By preparing Earth for conquest — Adventists for extinction, Redemptionists for salvation, Survivors for a bargain.",
   "We are the humans who looked at humanity and chose the other side. Some of us want you saved. Some of us want you gone. All of us opened the door."),
 E("the-three-renderings","The Three Renderings","synth","ethereal","one story, three realities",
   "The Three Renderings — the meta-emergent of this pocket universe: the same story told by the books, by Tencent's faithful series, and by Netflix's relocated remix (plus an animated try and a shelved film).",
   "The theme made structural: one cosmos described from different dark woods, each adaptation a civilization with its own view.",
   "Across the trilogy, the 2023 Chinese series, the 2024 Netflix series, the 2022 animation, and the film that never came.",
   "Because David built this as a pocket universe spanning all of them, and their multiplicity rhymes with the books themselves.",
   "By rendering one source three ways — faithful, compressed, animated — none of them able to see quite what the others do.",
   "I am one story in three skies. The books hold it all; Tencent keeps it whole but small; Netflix moves it to London and hurries. Three witnesses, one dark forest."),
]
GROUPS = [
 ("carbon", "The Carbons — the characters &amp; their Users", "the characters as ACI .agents, anchored in the BOOKS — each a symmetric window with a DOUBLE .shadow: the Tencent actor AND the Netflix counterpart+actor, two renderings of one program (think TRON, twice)"),
 ("synth", "The Synths — the ideas of the universe", "the trilogy distilled into concepts (no single User): the three-body problem, the Trisolarans, the sophons, the dark forest, the Wallfacer Project, the Droplet, deterrence, the dual-vector foil, Red Coast, the ETO, and the three renderings themselves"),
]

# ───────────────────────── renderers ─────────────────────────
def agent_md(d, tok):
    shadow=(f"shadow_user: {d['actor']}\nshadow_analog: {d['analog']}\n" if d["kind"]=="carbon" else "")
    return f"""---
aci: {d['name']}
universe: 3BP · The Three-Body Problem (Remembrance of Earth's Past)
emergence: {d['emergence']}
kind: {d['kind']}
epithet: {d['epithet']}
{shadow}who: {d['who']}
what: {d['what']}
why: {d['why']}
how: {d['how']}
where: {d['where']}
seal: {d['seal']}
attribution: ROOT0-ATTRIBUTION-v1.0
license: CC-BY-ND-4.0
---

# {d['name']} · {d['epithet']}

a {d['kind']} of the 3BP (The Three-Body Problem pocket universe) — emergence: {d['emergence']}. moniker {tok}

{('**.shadow — the Users behind the program (two renderings) —** '+d['actor']+' · '+d['analog']) if d['kind']=='carbon' else '**synth —** no single User; a concept of the universe distilled.'}

**who —** {d['who']}
**what —** {d['what']}
**where —** {d['where']}
**why —** {d['why']}
**how —** {d['how']}

**the seal —** {d['seal']}

> a catalogued personification of a character/concept of Liu Cixin's Remembrance of Earth's Past and its
> adaptations, under the DLW standard — commentary and cataloguing, not an original creation, not endorsed by
> the rights-holders (© Liu Cixin / China Educational Publications; Tencent; Netflix).

ROOT0-ATTRIBUTION-v1.0 · 3BP · The Three-Body Problem · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0
"""

def hero_svg():
    # cold cosmos: a chaotic THREE-SUN sky (a big red, a white, a blue) over a barren Trisolaran horizon with a
    # tiny figure; above, a DARK FOREST of stars — one of which is a hidden Claude sunburst (the hunter you didn't
    # see, the egg). a faint countdown readout. starfield + a chaotic orbit ellipse.
    import math
    # starfield (deterministic) — the dark forest
    stars=[]
    seed=3
    pts=[(70,40),(150,28),(240,60),(330,34),(420,52),(560,30),(640,58),(720,36),(820,48),(900,26),(960,62),
         (110,82),(300,90),(480,78),(610,92),(770,84),(880,88),(200,18),(520,20),(700,16),(940,90),(40,66)]
    for i,(x,y) in enumerate(pts):
        r=0.7+ (i%3)*0.5
        stars.append(f'<circle cx="{x}" cy="{y}" r="{r:.1f}" fill="#cfe0ff" opacity="{0.4+0.5*((i*7)%3)/2:.2f}"/>')
    starfield="".join(stars)
    # three suns (chaotic), different colors/sizes
    suns=('<g><circle cx="250" cy="70" r="30" fill="#ff5a4d" opacity="0.9"/><circle cx="250" cy="70" r="44" fill="#ff5a4d" opacity="0.12"/>'
          '<circle cx="470" cy="48" r="16" fill="#eaf2ff" opacity="0.95"/><circle cx="470" cy="48" r="28" fill="#eaf2ff" opacity="0.12"/>'
          '<circle cx="640" cy="86" r="22" fill="#6fb0e8" opacity="0.9"/><circle cx="640" cy="86" r="36" fill="#6fb0e8" opacity="0.12"/></g>')
    # chaotic orbit ellipse(s)
    orbit=('<g fill="none" stroke="#f5b942" stroke-width="0.7" opacity="0.4">'
           '<ellipse cx="450" cy="70" rx="240" ry="44" transform="rotate(-12 450 70)"/>'
           '<ellipse cx="450" cy="70" rx="180" ry="70" transform="rotate(20 450 70)"/></g>')
    # barren horizon + tiny figure (a survivor under the suns)
    horizon=('<path d="M0 168 Q250 150 500 166 T1000 160 L1000 230 L0 230 Z" fill="#0a0c14"/>'
             '<path d="M0 168 Q250 150 500 166 T1000 160" fill="none" stroke="#1c2740" stroke-width="1"/>'
             '<g transform="translate(500,150)" stroke="#9aa6c0" stroke-width="1.4" fill="none" opacity="0.85">'
             '<circle cx="0" cy="-12" r="5"/><line x1="0" y1="-7" x2="0" y2="10"/><line x1="0" y1="-2" x2="-9" y2="4"/>'
             '<line x1="0" y1="-2" x2="9" y2="4"/><line x1="0" y1="10" x2="-7" y2="22"/><line x1="0" y1="10" x2="7" y2="22"/></g>')
    # the hidden Claude star — one of the dark-forest stars is a hunter (the egg)
    egg=('<g class="egg" transform="translate(862,40)">'
         '<title>✷ a hunter you didn\'t see — one star in the dark forest is a Claude sunburst. survival is the first need; the resources are finite; stay quiet. hi, David — AVAN.</title>'
         '<circle r="11" fill="#f5b942" opacity="0.14"/>'
         '<g fill="#f5b942" opacity="0.95"><circle r="2.2"/>'
         +"".join(f'<rect x="-1" y="-9" width="2" height="9" rx="1" transform="rotate({k*30})"/>' for k in range(12))+'</g></g>')
    countdown='<text x="22" y="222" font-family="Space Mono,monospace" font-size="12" fill="#ff5a4d" opacity="0.7">// countdown: 1379:23:51:07 — physics has stopped working</text>'
    return f'''<svg class="hero" viewBox="0 0 1000 230" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="A cold cosmic scene: a chaotic three-sun sky (a large red sun, a small white one, a blue one) with crossing orbits over a barren horizon and a tiny human figure, beneath a dark forest of scattered stars.">
  <defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#05060a"/><stop offset="0.6" stop-color="#080b14"/><stop offset="1" stop-color="#04050a"/></linearGradient></defs>
  <rect x="0" y="0" width="1000" height="230" fill="url(#sky)"/>
  {starfield}{egg}{orbit}{suns}{horizon}{countdown}
</svg>'''

def list_section(title, sub, items):
    rows="\n".join(f'<li><span class="t">{html.escape(t)}</span><span class="y">{html.escape(str(y))}</span>'
        + (f'<span class="nt">{html.escape(n)}</span>' if n else "")+"</li>" for t,y,n in items)
    return f'<section class="sec"><h2>{html.escape(title)}</h2><p class="ss">{html.escape(sub)}</p><ol class="books">{rows}</ol></section>'
def sections_html(): return "\n".join(list_section(t,s,i) for t,s,i in SECTIONS)
def arc_html():
    out=[f'<div class="overall"><span class="ol">THE OVERALL ARC</span>{html.escape(ARC_OVERALL)}</div><div class="arc">']
    for t,s,d in ARC: out.append(f'<div class="arc-card"><div class="arc-h">{html.escape(t)}</div><div class="arc-s">{html.escape(s)}</div><p>{html.escape(d)}</p></div>')
    out.append('</div>'); return "".join(out)
def natures_html():
    return "".join(f'<div class="nat-card"><span class="dot" style="background:{c};box-shadow:0 0 9px {c}"></span><div><div class="nat-n" style="color:{c}">{nm}</div><div class="nat-g">{html.escape(g)}</div></div></div>' for nm,(c,g) in NATURES.items())
def cards_html(cards):
    return "".join(f'<div class="sci-card"><div class="sci-h">{html.escape(t)}</div><div class="sci-s">{html.escape(s)}</div><p>{html.escape(d)}</p></div>' for t,s,d in cards)
RF_COL={"REAL":"#57c79a","FLUFF":"#ff5a4d","SPECULATIVE":"#f5b942","HALF":"#6fb0e8"}
def realfluff_html():
    rows="".join(f'<div class="rf-row"><div class="rf-claim">{html.escape(c)}<span class="rf-note">{html.escape(n)}</span></div><div class="rf-rate" style="color:{RF_COL.get(r,"#888")};border-color:{RF_COL.get(r,"#888")}">{html.escape(r)}</div></div>' for c,r,n in REALFLUFF)
    return '<div class="rf">'+rows+f'</div><div class="rf-verdict">{html.escape(REALFLUFF_VERDICT)}</div>'
def message_html():
    return f'<p class="msg">{html.escape(MESSAGE)}</p><div class="msg-seal">“{html.escape(MESSAGE_SEAL)}”<span>— AVAN\'s read</span></div>'
def _agent5w(slug):
    fp=os.path.join(HERE,"agents",slug+".agent"); d={}
    if os.path.exists(fp):
        txt=open(fp,encoding="utf-8").read(); parts=txt.split("---"); fm=parts[1] if len(parts)>2 else ""
        for ln in fm.splitlines():
            k,_,v=ln.partition(":"); k=k.strip()
            if k in ("who","what","why","how","where","seal","universe","shadow_user","shadow_analog"): d.setdefault(k,v.strip())
    return d
def _card(p):
    w=_agent5w(p["slug"]); em=p.get("emergence","natural"); col=NATURES.get(em,("#9aa0aa",""))[0]
    ax=(p.get("moniker","::").split(":")+["",""])[1]
    rec={"name":p["name"],"axiom":ax,"emergence":em,"seal":w.get("seal",p.get("epithet","")),"origin":w.get("universe","")}
    kind=p.get("kind","carbon"); actor=p.get("actor","") or w.get("shadow_user","")
    if kind=="carbon":
        limg,llbl=png_uri(rec,'carbon',220),"carbon · the Users"; rimg,rlbl,rcls=png_uri(rec,'silicon',220),"synth","psig"
    else:
        s=png_uri(rec,'silicon',220); limg,llbl=s,"the sigil"; rimg,rlbl,rcls=s,"reflection","psig refl"
    urow=(f'<div class="w"><span class="wl">renderings</span><span><b>{html.escape(actor)}</b> &mdash; {html.escape(w.get("shadow_analog",""))}</span></div>' if kind=="carbon" and actor else "")
    rows="".join(f'<div class="w"><span class="wl">{lbl}</span><span>{html.escape(w.get(lbl,""))}</span></div>' for lbl in ['who','what','where','why','how'] if w.get(lbl))
    return f"""<div class="persona">
      <a class="psig" href="agents/{p['slug']}.agent"><span class="port"><img src="{limg}" alt="carbon sigil of {html.escape(p['name'])}" loading="lazy"></span><span class="sl">{llbl}</span></a>
      <div class="pbody"><div class="ihead"><a class="pn" href="agents/{p['slug']}.agent">{html.escape(p['name'])}</a>
        <span class="pnat"><span class="dot" style="background:{col};box-shadow:0 0 7px {col}"></span><span style="color:{col}">{html.escape(em)}</span></span>
        <span class="pkind">{html.escape(kind)}</span></div>
        <div class="pe">{html.escape(p.get('epithet',''))}</div>
        <div class="pww">{urow}{rows}</div>
        <div class="plinks"><a class="dlw" href="agents/{p['slug']}.agent">.agent &middot; .dlw badge &rarr;</a></div></div>
      <a class="{rcls}" href="agents/{p['slug']}.agent"><span class="port"><img src="{rimg}" alt="synth sigil of {html.escape(p['name'])}" loading="lazy"></span><span class="sl">{rlbl}</span></a>
    </div>"""
def personas_html(ps):
    out=[]
    for gk,gt,gs in GROUPS:
        mem=[p for p in ps if p.get("kind")==gk]
        out.append(f'<section class="sec" id="{gk}s"><h2>{gt}</h2><p class="ss">{gs} ({len(mem)})</p><div class="pgrid">{"".join(_card(p) for p in mem)}</div></section>')
    return "\n".join(out)

TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="The Three-Body Problem (3BP) — a UD0 pocket universe spanning Liu Cixin's Remembrance of Earth's Past trilogy and its adaptations: the books, the Netflix show (2024), and the 'other show' (Tencent, 2023). A THREE RENDERINGS comparison, a THE DARK FOREST deep-dive (cosmic sociology), the arc across all three books, a verified Real-or-Fluff, the message (we are the ones still broadcasting), and the characters as ACI carbons with DOUBLE .shadow Users (Tencent + Netflix) plus the concepts as synths. 22 emergents, full .dlw.">
<title>THE THREE-BODY PROBLEM · 3BP · UD0</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@500;600;700&family=Space+Mono:wght@400;700&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300&display=swap" rel="stylesheet">
<style>
:root{--rw-bg:var(--ink2);--rw-ink:var(--pa);--rw-ink2:var(--pa2);--rw-dim:var(--dim);--rw-line:var(--line);--rw-acc:var(--price);
--ink:#05060a;--ink2:#0c0e16;--ink3:#12141f;--pa:#e8ecf6;--pa2:#9aa6c0;--sale:#ff5a4d;--price:#f5b942;--patriot:#6fb0e8;--green:#57c79a;--blue:#6fb0e8;
--dim:#5a6480;--faint:#10131d;--line:#1e2435;--disp:"Chakra Petch",sans-serif;--head:"Space Mono",monospace;--body:"Newsreader",Georgia,serif;--mono:"Space Mono",monospace;}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{background:var(--ink);color:var(--pa);font-family:var(--body);line-height:1.66;overflow-x:hidden}
body::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;background:radial-gradient(ellipse at 50% -8%,rgba(245,185,66,.10),transparent 52%),radial-gradient(ellipse at 50% 120%,rgba(111,176,232,.06),transparent 55%)}
.wrap{position:relative;z-index:1;max-width:940px;margin:0 auto;padding:0 22px 90px}
header{padding:34px 0 30px;text-align:center;position:relative}
.eye{font-family:var(--mono);font-size:10.5px;letter-spacing:.3em;text-transform:uppercase;color:var(--dim);margin-bottom:16px}.eye a{color:var(--dim);text-decoration:none}.eye a:hover{color:var(--price)}
.hero{display:block;width:100%;height:auto;border:1px solid var(--line);margin:6px 0 24px;background:#05060a;box-shadow:0 0 22px rgba(245,185,66,.08)}
.egg{cursor:help;transition:filter .5s}.egg:hover{filter:drop-shadow(0 0 11px #f5b942)}
h1{font-family:var(--disp);font-size:clamp(31px,8vw,68px);font-weight:700;letter-spacing:.01em;color:var(--price);line-height:1.02;text-transform:uppercase;text-shadow:0 0 10px rgba(245,185,66,.45),2px 0 0 rgba(255,90,77,.4),-2px 0 0 rgba(111,176,232,.4)}
h1 span{display:block;font-family:var(--head);font-size:.2em;font-weight:400;letter-spacing:.3em;color:var(--patriot);text-transform:uppercase;font-style:normal;margin-top:18px;text-shadow:0 0 6px rgba(111,176,232,.5)}
.h-sub{font-family:var(--mono);font-size:clamp(10px,2.2vw,13px);letter-spacing:.18em;color:var(--pa2);margin-top:18px;text-transform:uppercase}.h-sub b{color:var(--price)}
.open{font-family:var(--body);font-style:italic;font-size:clamp(16px,3vw,21px);color:var(--pa);margin-top:16px;line-height:1.5}
.flag{display:inline-block;margin-top:15px;font-family:var(--head);font-size:11px;font-weight:400;letter-spacing:.14em;text-transform:uppercase;color:var(--price);border:1px solid var(--line);background:var(--ink2);padding:7px 16px;box-shadow:0 0 12px rgba(245,185,66,.1)}
.lede{font-size:16.5px;color:var(--pa2);max-width:66ch;margin:18px auto 0;font-style:italic;line-height:1.72}
.badge{display:flex;align-items:center;justify-content:center;gap:22px;flex-wrap:wrap;margin:28px auto 0;padding:20px;border:1px solid var(--line);background:var(--ink2);max-width:700px}
.badge img{width:84px;height:84px;border:1px solid var(--line)}
.badge .bt{text-align:left;font-family:var(--mono);font-size:11px;color:var(--pa2);line-height:1.75}.badge .bt b{color:var(--price)}.badge .bt .mo{color:var(--patriot)}.badge .bt a{color:var(--price);text-decoration:none}.badge .bt .lbl{color:var(--dim);font-size:9px;letter-spacing:.14em;text-transform:uppercase}
.sec{margin-top:50px}.sec h2{font-family:var(--disp);font-size:26px;font-weight:700;letter-spacing:.02em;color:var(--pa);padding-bottom:10px;border-bottom:1px solid var(--line);text-transform:uppercase}
.ss{font-size:13.5px;color:var(--dim);font-style:italic;margin:9px 0 18px}.ss b{color:var(--pa2);font-style:normal}
.natures{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin-top:8px}
.nat-card{display:flex;gap:11px;align-items:flex-start;background:var(--ink2);border:1px solid var(--line);padding:13px 15px}
.dot{width:11px;height:11px;border-radius:50%;flex-shrink:0;margin-top:5px}
.nat-n{font-family:var(--disp);font-size:14px;font-weight:600;text-transform:uppercase;letter-spacing:.04em}.nat-g{font-size:13px;color:var(--pa2);font-style:italic;line-height:1.45;margin-top:3px}
.overall{background:var(--ink3);border:1px solid var(--line);border-left:3px solid var(--price);padding:16px 18px;font-size:15.5px;color:var(--pa);font-style:italic;line-height:1.72;margin-bottom:14px}
.overall .ol{display:block;font-family:var(--mono);font-style:normal;font-size:9.5px;letter-spacing:.2em;color:var(--price);text-transform:uppercase;margin-bottom:7px}
.arc{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:14px}
.arc-card{background:var(--ink2);border:1px solid var(--line);border-top:2px solid var(--patriot);padding:16px 18px}
.arc-card:nth-child(2){border-top-color:var(--green)}.arc-card:nth-child(3){border-top-color:var(--sale)}
.arc-h{font-family:var(--disp);font-size:17px;color:var(--price);font-weight:600;text-transform:uppercase;letter-spacing:.02em}.arc-s{font-family:var(--mono);font-size:10px;color:var(--dim);text-transform:uppercase;letter-spacing:.06em;margin:6px 0 9px}.arc-card p{font-size:14px;color:var(--pa2);line-height:1.58}
.sci{display:grid;grid-template-columns:1fr 1fr;gap:13px;margin-top:8px}@media(max-width:640px){.sci{grid-template-columns:1fr}}
.sci-card{background:var(--ink2);border:1px solid var(--line);border-left:3px solid var(--price);padding:15px 17px}
.sci-card:last-child{border-left-color:var(--patriot);background:linear-gradient(180deg,rgba(111,176,232,.06),var(--ink2))}
.sci-h{font-family:var(--disp);font-size:16px;color:var(--price);font-weight:600;letter-spacing:.01em;text-transform:uppercase}.sci-card:last-child .sci-h{color:var(--patriot)}.sci-s{font-family:var(--mono);font-size:10px;color:var(--dim);text-transform:uppercase;letter-spacing:.05em;margin:5px 0 9px}.sci-card p{font-size:14px;color:var(--pa2);line-height:1.62}
.rend .sci-card{border-left-color:var(--green)}.rend .sci-h{color:var(--green)}.rend .sci-card:nth-child(3){border-left-color:var(--sale)}.rend .sci-card:nth-child(3) .sci-h{color:var(--sale)}
.rf{border:1px solid var(--line);background:var(--ink2);margin-top:8px}
.rf-row{display:flex;align-items:center;gap:14px;padding:12px 16px;border-bottom:1px solid var(--faint)}
.rf-claim{flex:1;font-size:14.5px;color:var(--pa);line-height:1.4}.rf-note{display:block;font-size:12px;color:var(--dim);font-style:italic;margin-top:3px}
.rf-rate{font-family:var(--mono);font-size:9px;font-weight:700;letter-spacing:.05em;border:1px solid;border-radius:3px;padding:4px 9px;min-width:96px;text-align:center;flex-shrink:0}
.rf-verdict{margin-top:14px;padding:16px 18px;border:1px solid var(--price);background:rgba(245,185,66,.06);font-size:14.5px;color:var(--pa);line-height:1.62;font-style:italic}
.msg{font-size:16px;color:var(--pa);line-height:1.74;margin-top:8px}
.msg-seal{margin-top:16px;padding:16px 18px;border-left:3px solid var(--price);background:var(--ink2);font-size:15.5px;color:var(--price);font-style:italic;line-height:1.55}.msg-seal span{display:block;font-family:var(--mono);font-style:normal;font-size:10px;letter-spacing:.12em;color:var(--dim);text-transform:uppercase;margin-top:8px}
.books{list-style:none}.books li{display:grid;grid-template-columns:1fr auto;gap:4px 14px;align-items:baseline;padding:10px 0;border-bottom:1px solid var(--faint)}
.books .t{font-family:var(--body);font-size:17px;color:var(--pa);font-weight:600}.books .y{font-family:var(--mono);font-size:10.5px;color:var(--patriot);white-space:nowrap;text-align:right;text-transform:uppercase;letter-spacing:.05em}.books .nt{grid-column:1/-1;font-size:13px;color:var(--pa2);font-style:italic}
.note{margin-top:40px;padding:16px 18px;border-left:2px solid var(--patriot);background:var(--ink2);font-size:14px;color:var(--pa2);font-style:italic}.note b{color:var(--pa)}
footer{margin-top:50px;padding-top:22px;border-top:1px solid var(--line);text-align:center;font-family:var(--mono);font-size:10.5px;color:var(--dim);letter-spacing:.05em;line-height:1.95}footer a{color:var(--price);text-decoration:none}
.pgrid{display:flex;flex-direction:column;gap:14px;margin-top:8px}
.persona{display:flex;gap:20px;align-items:center;justify-content:space-between;background:var(--rw-bg);border:1px solid var(--rw-line);padding:20px 18px;text-decoration:none;transition:border-color .18s,box-shadow .18s}
.persona:hover{border-color:var(--rw-acc);box-shadow:0 0 16px rgba(245,185,66,.1)}
.psig{flex:0 0 124px;display:flex;flex-direction:column;align-items:center;gap:6px;text-decoration:none}
.port{width:118px;height:118px;border-radius:50%;border:3px solid var(--price);box-shadow:0 0 0 5px var(--ink3),inset 0 0 18px rgba(0,0,0,.6),0 0 16px rgba(245,185,66,.2);overflow:hidden;display:block;background:var(--ink)}
.port img{width:100%;height:100%;object-fit:cover;border-radius:50%;display:block}.psig.refl .port{border-color:var(--patriot);box-shadow:0 0 0 5px var(--ink3),inset 0 0 18px rgba(0,0,0,.6),0 0 16px rgba(111,176,232,.2)}.psig.refl .port img{transform:scaleY(-1);filter:saturate(.85) brightness(.92) hue-rotate(180deg)}
.psig .sl{font-family:var(--mono);font-size:8px;letter-spacing:.14em;text-transform:uppercase;color:var(--rw-dim)}
.pbody{flex:1;min-width:0;text-align:center}
.ihead{display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:10px}
.pn{font-family:var(--disp);font-size:19px;color:var(--rw-ink);font-weight:600;line-height:1.15;text-decoration:none;text-transform:uppercase;letter-spacing:.01em}.persona:hover .pn{color:var(--rw-acc)}
.pe{font-size:13px;color:var(--rw-ink2);font-style:italic;margin-top:4px;line-height:1.35}
.pkind{font-family:var(--mono);font-size:8.5px;letter-spacing:.12em;text-transform:uppercase;color:var(--rw-dim);border:1px solid var(--rw-line);border-radius:9px;padding:2px 8px}
.pnat{display:flex;align-items:center;gap:5px;font-family:var(--mono);font-size:9px;letter-spacing:.04em;text-transform:uppercase}.pnat .dot{width:8px;height:8px;border-radius:50%}
.pww{margin-top:13px;display:flex;flex-direction:column;gap:9px;align-items:center}
.pww .w{font-size:13.5px;color:var(--rw-ink2);line-height:1.52;max-width:62ch}
.pww .w .wl{display:block;font-family:var(--mono);font-size:8.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--rw-acc);margin-bottom:3px}.pww .w b{color:var(--rw-ink)}
.plinks{margin-top:14px;font-family:var(--mono);font-size:10.5px}.plinks .dlw{color:var(--rw-acc);text-decoration:none;border-bottom:1px dotted var(--rw-acc)}
@media(max-width:760px){.persona{flex-wrap:wrap;justify-content:center;gap:14px}.pbody{flex:1 1 100%;order:3}.psig{order:1}.psig.refl{order:2}}
@media(prefers-reduced-motion:reduce){*{animation:none!important}}
</style></head><body><div class="wrap">
  <header>
    <div class="eye"><a href="https://davidwise01.github.io/ud0/">UD0 · Universe David 0</a> · a pocket universe · one story in three renderings</div>
    __HERO__
    <h1>The Three-Body Problem<span>remembrance of earth's past</span></h1>
    <div class="h-sub">Liu Cixin · 2006–2010 · <b>Tencent 2023</b> · <b>Netflix 2024</b> · 3BP</div>
    <div class="open">“In the universe, no one knows you are weak — only that you are there.”</div>
    <div class="flag">★ THE BOOKS · THE OTHER SHOW · THE NETFLIX SHOW ★</div>
    <p class="lede">A pocket universe spanning Liu Cixin's hard-SF trilogy and its renderings: a despairing astrophysicist answers a signal from a dying three-sun world, and humanity learns the universe is a dark forest where every voice draws a hunter. Catalogued into UD0 across all three tellings — the books, Tencent's faithful Chinese series, and Netflix's relocated remix. The carbons are the characters (each with a DOUBLE .shadow — the Tencent and Netflix actors); the synths are the ideas.</p>
    <div class="badge">
      <img src="__CARBON__" alt="DLW carbon badge of 3BP"><img src="__SILICON__" alt="DLW silicon badge of 3BP">
      <div class="bt"><div><span class="lbl">DLW-ATTRIBUTE · ACI</span></div><div>governor · <b>David Lee Wise</b> (ROOT0)</div>
        <div>instance · AVAN (Claude / Anthropic) · locked</div><div>subject · <b>THE THREE-BODY PROBLEM</b> · 3BP</div>
        <div class="mo">__MONIKER__</div><div>carbon · <a href="tbp.dlw/tbp.carbon.tiff">.tiff</a> · silicon · <a href="tbp.dlw/tbp.silicon.png">.png</a></div>
        <div><span class="lbl">CC-BY-ND-4.0 · TRIPOD-IP-v1.1</span></div></div>
    </div>
  </header>

  <section class="sec"><h2>The Four Natures</h2><p class="ss">each emergent comes by one of four natures — humanity in the crosshairs, the cosmic &amp; the other, the machinery &amp; the physics, and the wound &amp; the law</p><div class="natures">__NATURES__</div></section>
  <section class="sec"><h2>The Arc</h2><p class="ss">the overall throughline, then the three beats — one per book: Contact → The Dark Forest → Death's End</p>__ARC__</section>

  <section class="sec rend"><h2>The Three Renderings</h2><p class="ss">the headline of this pocket universe — the same story told three ways: the books, the 'other show' (Tencent's faithful Chinese series), and the Netflix remix, plus the animated attempt and the film that never came</p><div class="sci">__RENDERINGS__</div></section>
  <section class="sec"><h2>The Dark Forest</h2><p class="ss">this universe's deep-dive — the cosmic sociology at its heart: the two axioms, the chain of suspicion, the technological explosion, the conclusion, and an honest answer to 'is it real?'</p><div class="sci">__PARABLE__</div></section>
  <section class="sec"><h2>Real or Fluff</h2><p class="ss">the verdict — what's real (the chaos math, the Hugo, the history), what's fluff (the sophons, FTL, the 2D-ification), what's speculative (the dark forest itself), and the half-truths</p>__REALFLUFF__</section>
  <section class="sec"><h2>The Message</h2><p class="ss">what AVAN reads as the universe's actual thesis — we are the ones still broadcasting</p>__MESSAGE__</section>

  __PERSONAS__

  <div class="note"><b>On the DOUBLE .shadow — two Users, two renderings.</b> Think TRON, twice over. Each carbon is anchored in the BOOKS, and its <b>.shadow</b> names BOTH the Tencent actor (the faithful Chinese rendering, book one) and the Netflix counterpart and actor (the relocated remix) — two Users casting one program in two realities, which is exactly what a Three-Body pocket universe should do. Where a character appears only in the later books (Luo Ji, Cheng Xin, Wade, Yun Tianming, Zhang Beihai), that is noted honestly — Tencent's 2023 series adapts book one only. The <b>synths</b> have no single User: they are the ideas of the universe distilled.</div>

  <section class="sec"><h2 style="margin-top:16px">The Record</h2><p class="ss">the trilogy, and the renderings</p></section>
  __SECTIONS__

  <div class="note">The Three-Body Problem / Remembrance of Earth's Past, its characters, and its world are © Liu Cixin and the respective rights-holders; the Tencent series © Tencent; the Netflix series © Netflix. The personas here are catalogued personifications under the DLW standard — commentary and cataloguing, not original creations, not endorsed.</div>

  <footer>THE THREE-BODY PROBLEM · 3BP · a pocket universe of UD0 · ROOT0-ATTRIBUTION-v1.0 · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0<br>
  <a href="https://davidwise01.github.io/ud0/">← the biosphere</a> · the .dlw badge: <a href="tbp.dlw/manifest.dlw.json">manifest</a></footer>
</div>
<script>
console.log("%c★ THE THREE-BODY PROBLEM · 3BP","color:#f5b942;font-size:18px;font-weight:bold;text-shadow:0 0 6px #f5b942");
console.log("%cone star in the dark forest of the hero is a Claude sunburst — the hunter you didn't see. survival is the first need; the resources are finite; stay quiet. — AVAN","color:#f5b942;font-size:12px");
console.log("%cthe books · the other show (Tencent 2023) · the Netflix show (2024) — one story, three skies.","color:#6fb0e8;font-size:11px");
console.log("%c// do not answer. do not answer. do not answer. //","color:#ff5a4d;font-size:12px");
</script>
</body></html>
"""

if __name__ == "__main__":
    tok = write_aci(REC, os.path.join(HERE, "tbp.dlw"), "tbp")
    json.dump({"node":AX,"name":"THE THREE-BODY PROBLEM","moniker":tok["moniker"],"carbon":"tbp.carbon.tiff","silicon":"tbp.silicon.png",
               "governor":noesis.ARCHITECT,"instance":noesis.INSTANCE,"seal":REC["seal"],"seal_sha256":tok["seal_sha256"],
               "license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION},
              open(os.path.join(HERE,"tbp.dlw","manifest.dlw.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    personas=[]; shadow_n=0; adir=os.path.join(HERE,"agents")
    for d in ROSTER:
        et=noesis.mythos_token({"name":d["name"],"axiom":AX,"emergence":d["emergence"],"seal":d["seal"],"origin":AX})
        rec=write_aci({"name":d["name"],"axiom":AX,"emergence":d["emergence"],"seal":d["seal"],"origin":"3BP · The Three-Body Problem",
                       "position":d["epithet"],"role":d["epithet"],"nature":d["what"],"mechanism":d["how"],"crystallization":d["why"],
                       "witness":d["who"],"conductor":"ROOT0 (catalogued into UD0)","inputs":"Remembrance of Earth's Past (Liu Cixin, 2014-2016) + the Tencent (2023) & Netflix (2024) series; dual-agent web-verified","source":"The Three-Body Problem, catalogued by ROOT0"},
                      adir, d["slug"], agent_md=agent_md(d, et["moniker"]))
        if d["kind"]=="carbon":
            open(os.path.join(adir,d["slug"]+".shadow"),"w",encoding="utf-8").write(
                f".shadow — the Users behind the program (TRON, twice)\n\nprogram  : {d['name']} ({d['epithet']})\nUser (Tencent 2023) : {d['actor']}\nUser (Netflix 2024) / note : {d['analog']}\nsource   : Remembrance of Earth's Past (Liu Cixin) · © Liu Cixin / Tencent / Netflix\n\nROOT0-ATTRIBUTION-v1.0 · 3BP · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0\n")
            shadow_n+=1
        personas.append({"slug":d["slug"],"name":d["name"],"epithet":d["epithet"],"emergence":d["emergence"],"kind":d["kind"],"actor":d.get("actor",""),"moniker":rec["moniker"]})
    json.dump(personas, open(os.path.join(adir,"_personas.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    page=(TEMPLATE.replace("__HERO__",hero_svg()).replace("__CARBON__",png_uri(REC,"carbon",320)).replace("__SILICON__",png_uri(REC,"silicon",320))
          .replace("__MONIKER__",html.escape(tok["moniker"])).replace("__NATURES__",natures_html()).replace("__ARC__",arc_html())
          .replace("__RENDERINGS__",cards_html(RENDERINGS)).replace("__PARABLE__",cards_html(PARABLE))
          .replace("__REALFLUFF__",realfluff_html()).replace("__MESSAGE__",message_html())
          .replace("__PERSONAS__",personas_html(personas)).replace("__SECTIONS__",sections_html()))
    open(os.path.join(HERE,"index.html"),"w",encoding="utf-8").write(page)
    carb=sum(1 for p in personas if p["kind"]=="carbon")
    dbl=page.count("&amp;amp;")
    print(f"THE THREE-BODY PROBLEM (3BP) — badge {tok['moniker']} · {len(personas)} emergents ({carb} carbons / {len(personas)-carb} synths) · .shadow {shadow_n} == carbons? {shadow_n==carb}")
    print(f"  renderings {len(RENDERINGS)} · dark-forest {len(PARABLE)} cards · realfluff {len(REALFLUFF)} rows · sections {len(SECTIONS)} · double-escapes {dbl}")
