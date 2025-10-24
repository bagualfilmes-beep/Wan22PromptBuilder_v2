import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import random
import pyperclip

# ============================================================
# WAN_PROMPTS_V2
#
# Linguagem focada para Wan 2.2:
# - Cinematic realism
# - i2v/t2v behavior control
# - Stable body/face identity
# - Camera / lens / lighting vocab that models like Wan 2.2,
#   Pika, Kling, Runway Gen-3 tend to respect.
#
# Todas as frases em inglês técnico e direto, sem floreio artístico
# e sem estilos cartoon/anime/pintura.
# ============================================================

WAN_PROMPTS_V2 = {
    "style": [
        "cinematic ultra realistic look, natural skin texture, subtle film grain",
        "high-end commercial beauty look, glossy clean advertising aesthetic",
        "soft intimate cinematic mood, warm and inviting atmosphere",
        "moody dramatic tone, desaturated cool shadows, emotional realism",
        "fashion editorial look, controlled lighting, polished high-end presentation",
        "documentary-style natural realism, minimal stylization, lifelike motion",
        "romantic warm tone, gentle highlights, soft glow on skin",
        "premium product commercial aesthetic, smooth gradients, flawless rendering",
        "intimate private moment tone, low noise, quiet emotional atmosphere",
        "soft highlight rolloff on skin, flattering beauty lighting, no harsh edges",
        "cinematic realism, stabilized body motion, physically correct shading",
        "slow sensual cinematic pacing, elegant controlled presence",
    ],

    "camera": [
        # Angle, framing, movement
        "chest-up framing, upper body only, subject centered, camera locked steady",
        "medium close-up shot, gentle handheld sway, natural breathing motion",
        "slow cinematic dolly-in toward the subject, smooth forward drift",
        "slow push-in shot from in front of the subject, subtle forward motion",
        "locked tripod shot, stable frame, zero shake, interview-style camera",
        "handheld close-up, natural micro-shake, intimate presence",
        "over-the-shoulder shot, main subject in foreground, second subject soft in background",
        "low-angle hero framing, camera slightly below chin line looking upward",
        "slightly high angle down toward the subject, flattering beauty perspective",
        "profile side shot, camera parallel to face and shoulders, elegant attitude",
        "soft pan to the right, slow lateral camera drift, cinematic pacing",
        "soft pan to the left, extremely slow lateral movement, controlled tone",
        "subtle tilt down across the subject’s body, smooth and elegant motion",
        "frontal facing angle, subject squared to camera, centered presence",
        "camera remains in front of subject, no orbit, frontal focus only",
    ],

    "lens": [
        # Focal length / depth of field
        "85mm portrait lens look, shallow depth of field, creamy background blur",
        "50mm standard cinematic lens, natural perspective, gentle focus falloff",
        "35mm handheld documentary look, close immersive perspective",
        "telephoto compression, background pushed in, flattering facial geometry",
        "soft bokeh background, high aperture blur, cinematic isolation of subject",
        "macro-style detail emphasis, extremely shallow depth, intimate feel",
        "neutral focal length ~50mm, commercial interview aesthetics",
        "tight portrait framing ~85mm, emphasis on face and shoulders",
        "medium telephoto aesthetic, flattering jawline and cheekbones",
        "depth of field focused on eyes, slight blur on hair and neck",
    ],

    "lighting": [
        # Cinematic light setups
        "soft warm backlight creating a rim on hair and shoulders, subtle glow",
        "diffused golden-hour lighting, warm highlights, no harsh shadows",
        "studio softbox key light from the front, even flattering illumination",
        "beauty lighting, frontal soft fill, no deep facial shadows",
        "moody side lighting, one side lit, the other side falling into shadow",
        "neon-style colored accent light from the side, cinematic nightlife vibe",
        "warm lamp light from below frame, cozy interior evening mood",
        "cool blue ambient fill plus warm key light, cinematic color contrast",
        "soft rim light from behind, gentle halo around hair and shoulders",
        "low intensity ambient fill, dim intimate atmosphere, gentle falloff",
        "candlelit warmth, flickering amber tones, sensual proximity feel",
        "indirect bounced light, realistic and diffuse, no harsh edges",
        "backlit silhouette with gentle edge light, face still slightly visible",
        "high gloss highlight on skin, controlled specular reflection",
    ],

    "environment": [
        # Scene / background / atmosphere
        "neutral indoor background, minimal distractions, softly out of focus",
        "intimate bedroom interior, warm lamp light, shallow depth of field",
        "softly lit studio backdrop, elegant and minimal, no clutter in frame",
        "modern apartment interior at night, warm lamps, cinematic cozy mood",
        "indoor low light setting, warm edge light and deep background falloff",
        "urban night street background, blurred neon signage and wet reflections",
        "soft sunset glow through a window, golden backlight haze",
        "close indoor framing, background almost entirely blurred, personal atmosphere",
        "private indoor setting, intimate mood, low ambient light",
        "luxury interior aesthetic, smooth surfaces and warm highlights",
        "soft haze in the background, atmospheric depth in the air",
        "nighttime ambient urban light, colored reflections, slight humidity in air",
        "commercial studio product-shot vibe, neutral backdrop, clean presentation",
        "subtle reflective surfaces catching warm light behind the subject",
    ],

    "character": [
        # Behavior, identity consistency, gaze
        "keep the exact same face identity as the reference image, do not alter facial structure, skin tone, makeup or hairstyle",
        "maintain same hairstyle, same facial proportions, same makeup look, no morphing",
        "the subject keeps steady eye contact with the viewer, eyes open, neutral mouth, calm expression",
        "upper body only (chest-up framing), do not zoom out to full body, keep framing tight",
        "the subject breathes softly, subtle chest motion, natural realism",
        "slow confident posture, relaxed shoulders, sensual controlled movement",
        "no exaggerated facial expression, maintain subtle confidence, no cartoon emotion",
        "slight head tilt downward while eyes still look directly at the viewer, intimate feel",
        "final frame: same face identity, same hairstyle, same makeup look, same lighting mood",
        "the subject gently shifts weight from one hip to the other, minimal movement, controlled pacing",
        "the subject keeps lips slightly parted, subtle and calm, not smiling",
        "no fast approach toward the camera, body mostly in place, controlled presence",
        "hands remain natural and anatomically correct, no distortion, no extra fingers",
        "no covering of the face with hands or objects, keep face fully visible",
    ],

    "interaction": [
        # Multi-person direction / staging
        "male enters from the viewer’s right side and positions himself behind the female subject, staying behind her body, never blocking her face",
        "the second person places both hands gently at her waist from behind, hands visible but not covering her chest or face, natural relaxed contact",
        "both characters remain chest-up framed, aligned in the center of the shot, shared intimate presence",
        "the supporting character stays slightly behind and offset, keeping the main subject as the visual focus",
        "the main subject remains dominant in frame, the second person is supportive background presence",
        "soft body contact, no aggressive motion, calm synchronized breathing pace",
        "the secondary subject leans in from behind her shoulder, face close but not overlapping her face, no face obstruction",
        "two-person framing where the primary subject faces the camera and the partner is slightly behind, affectionate protective posture",
        "the partner stays behind her, aligned chest-to-back, never crossing in front of her or blocking camera view",
        "subtle guiding touch at the waist or hips, hands naturally shaped, intimate but controlled energy",
        "eye contact remains primarily on the main subject, not on the supporting one",
        "the final frame maintains both in shot, but the main subject is still the hero focus",
    ],

    "composition": [
        # Framing, palette, grading, visual priority
        "centered composition, subject in the middle of frame, chest-up crop, balanced negative space",
        "rule-of-thirds style framing, subject slightly off-center, cinematic asymmetry",
        "shallow depth of field with creamy background bokeh, attention locked on subject",
        "soft warm color palette with subtle highlights on skin, inviting tone",
        "muted desaturated background with warm skin highlights in the foreground",
        "cinematic contrast grade with lifted shadows and controlled specular highlights",
        "gentle highlight rolloff, no blown-out hotspots, professional beauty lighting finish",
        "framing keeps shoulders and collarbone visible, intimate portrait energy",
        "slow sensual pacing, no chaotic movement, elegant presentation",
        "the subject remains the hero of the frame, background always secondary",
        "soft foreground blur partially framing the subject, voyeuristic intimacy",
        "natural color grading, realistic skin tone, no oversaturation",
        "final frame should feel like a still from a high-end cinematic commercial shoot",
    ],

    "timing": [
        # Motion pacing / realism of movement
        "slow cinematic tempo, consistent frame pacing, no sudden jumps",
        "very gentle idle body motion, natural breathing and micro-adjustments",
        "smooth transition from stillness into slight torso turn, elegant and controlled",
        "realistic body inertia, torso moves first, head follows with a slight delay",
        "slow pan timing, camera drifting without abrupt acceleration or stops",
        "subtle forward push-in across several seconds, cinematic tension build",
        "no fast zooms, no snap cuts, maintain a calm sensual rhythm",
        "deliberate, unhurried physical motion, expressive but not exaggerated",
        "soft micro-sway in the camera to mimic handheld realism",
        "final moment pauses on the subject, holding eye contact for emphasis",
    ],

    "special": [
        # Cinematic tricks / shot language
        "cinematic zoom timing, gradual push toward the subject over several seconds",
        "focus pull from background subject to foreground subject, smooth and precise",
        "depth shift cue: foreground blur becomes sharp while background falls out of focus",
        "slow motion emphasis on hair movement and fabric motion, elegant slow dynamics",
        "subtle lens breathing effect during focus changes, realistic optical behavior",
        "light catching moisture on skin, glossy specular highlights, sensual texture",
        "soft atmospheric haze in the background, volumetric depth and air density",
        "gently reflective surfaces in the back of frame, creating cinematic light streaks",
        "intimate POV-like framing, viewer feels physically close to the subject",
        "final frame held as if it's a cinematic key shot, hero moment freeze",
    ]
}


# ============================================================
# ORDER OF TABS AND DISPLAY NAMES
# ============================================================

TAB_ORDER_V2 = [
    ("style",       "🎨 Style / Look"),
    ("camera",      "🎥 Camera / Angle / Motion"),
    ("lens",        "📷 Lens / Focal / DOF"),
    ("lighting",    "💡 Lighting"),
    ("environment", "🌍 Environment / Scene"),
    ("character",   "🧍 Character / Consistency"),
    ("interaction", "🧍‍♂️🧍‍♀️ Interaction / Staging"),
    ("composition", "🎯 Composition / Color / Grade"),
    ("timing",      "⏱️ Timing / Motion Style"),
    ("special",     "✨ Special Cues / Cinematic Tricks"),
]


# ============================================================
# UI COMPONENT: CategoryTab
# ============================================================

class CategoryTab(tk.Frame):
    """
    A single tab with:
    - Search field (filters inside this tab)
    - Scrollable list of prompts for that category
    - Selection memory
    - Double-click copies a snippet immediately
    """
    def __init__(self, master, cat_key, title, prompts_list, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.cat_key = cat_key
        self.title = title
        self.all_items = prompts_list[:]      # full list
        self.filtered_items = prompts_list[:] # current filtered view
        self.selected_prompt = None

        self.configure(bg="#1e1e1e")

        # label + search field
        tk.Label(
            self,
            text=f"Search in {title}:",
            bg="#1e1e1e",
            fg="white"
        ).pack(anchor="w", padx=10, pady=(10, 2))

        self.search_var = tk.StringVar()
        entry = tk.Entry(self, textvariable=self.search_var, width=50)
        entry.pack(anchor="w", padx=10, pady=(0, 8))
        entry.bind("<KeyRelease>", self.on_search_change)

        # listbox + scrollbar
        list_frame = tk.Frame(self, bg="#1e1e1e")
        list_frame.pack(fill="both", expand=True, padx=10, pady=(0,10))

        self.listbox = tk.Listbox(
            list_frame,
            selectmode=tk.SINGLE,
            activestyle="dotbox",
            bg="#252526",
            fg="#d4d4d4",
            width=100,
            height=15
        )
        self.listbox.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(list_frame, command=self.listbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.listbox.config(yscrollcommand=scrollbar.set)

        # events
        self.listbox.bind("<<ListboxSelect>>", self.on_select)
        self.listbox.bind("<Double-Button-1>", self.on_double_click)

        # initialize with all items
        self.refresh_listbox()

    def refresh_listbox(self):
        self.listbox.delete(0, tk.END)
        for item in self.filtered_items:
            self.listbox.insert(tk.END, item)

    def on_search_change(self, event=None):
        query = self.search_var.get().strip().lower()
        if not query:
            self.filtered_items = self.all_items[:]
        else:
            self.filtered_items = [p for p in self.all_items if query in p.lower()]
        self.refresh_listbox()

    def on_select(self, event=None):
        sel = self.listbox.curselection()
        if sel:
            idx = sel[0]
            if 0 <= idx < len(self.filtered_items):
                self.selected_prompt = self.filtered_items[idx]

    def on_double_click(self, event=None):
        sel = self.listbox.curselection()
        if sel:
            idx = sel[0]
            if 0 <= idx < len(self.filtered_items):
                text_to_copy = self.filtered_items[idx]
                pyperclip.copy(text_to_copy)
                messagebox.showinfo("Copied", "Snippet copied to clipboard.")

    def get_selected(self):
        return self.selected_prompt


# ============================================================
# APP CLASS
# ============================================================

class Wan22PromptBuilderAppV2(tk.Tk):
    def __init__(self, prompts_dict):
        super().__init__()
        self.prompts_dict = prompts_dict
        self.title("Wan 2.2 Prompt Builder v2")
        self.geometry("1100x780")
        self.configure(bg="#1e1e1e")

        # style notebook (dark tabs)
        style = ttk.Style()
        style.theme_use("default")
        style.configure("TNotebook", background="#1e1e1e", borderwidth=0)
        style.configure("TNotebook.Tab",
                        background="#2d2d30",
                        foreground="#ffffff",
                        padding=(10,6))
        style.map("TNotebook.Tab",
                  background=[("selected", "#3a3a3d")],
                  foreground=[("selected", "#ffffff")])

        # notebook with all tabs
        self.tabs = {}
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)

        for (cat_key, nice_name) in TAB_ORDER_V2:
            items = prompts_dict.get(cat_key, [])
            tab = CategoryTab(self.notebook, cat_key, nice_name, items, bg="#1e1e1e")
            self.notebook.add(tab, text=f"{nice_name} ({len(items)})")
            self.tabs[cat_key] = tab

        # bottom action bar
        bottom_frame = tk.Frame(self, bg="#1e1e1e")
        bottom_frame.pack(fill="x", padx=10, pady=(0,10))

        tk.Button(
            bottom_frame,
            text="🎲 Random Wan 2.2 Scene",
            command=self.compose_random,
            width=22
        ).pack(side="left", padx=5)

        tk.Button(
            bottom_frame,
            text="🧩 Build From Selected",
            command=self.compose_selected,
            width=22
        ).pack(side="left", padx=5)

        tk.Button(
            bottom_frame,
            text="📋 Copy Prompt",
            command=self.copy_full,
            width=14
        ).pack(side="left", padx=5)

        tk.Button(
            bottom_frame,
            text="💾 Save Favorite",
            command=self.save_favorite,
            width=16
        ).pack(side="left", padx=5)

        # output box
        self.output_box = scrolledtext.ScrolledText(
            self,
            wrap=tk.WORD,
            width=130,
            height=10,
            bg="#252526",
            fg="#d4d4d4",
            font=("Consolas", 10)
        )
        self.output_box.pack(fill="both", expand=False, padx=10, pady=(0,10))

    def _compose_from_parts(self, parts_dict):
        # Build final prompt in a fixed order that Wan 2.2 tends to parse well.
        order = [c[0] for c in TAB_ORDER_V2]
        chosen = []
        for cat_key in order:
            text = parts_dict.get(cat_key)
            if text:
                chosen.append(text.strip())
        # One clean line, safe to paste into ComfyUI / SeaArt.
        return ", ".join(chosen)

    def compose_selected(self):
        chosen_parts = {}
        for cat_key, _nice in TAB_ORDER_V2:
            tab = self.tabs.get(cat_key)
            if tab:
                sel = tab.get_selected()
                if sel:
                    chosen_parts[cat_key] = sel
        final_prompt = self._compose_from_parts(chosen_parts)
        self.output_box.delete(1.0, tk.END)
        if final_prompt:
            self.output_box.insert(tk.END, final_prompt)
        else:
            self.output_box.insert(tk.END, "No selection in tabs.")

    def compose_random(self):
        chosen_parts = {}
        for cat_key, _nice in TAB_ORDER_V2:
            items = self.prompts_dict.get(cat_key, [])
            if items:
                chosen_parts[cat_key] = random.choice(items)
        final_prompt = self._compose_from_parts(chosen_parts)
        self.output_box.delete(1.0, tk.END)
        if final_prompt:
            self.output_box.insert(tk.END, final_prompt)
        else:
            self.output_box.insert(tk.END, "Not enough prompts to build random scene.")

    def copy_full(self):
        textval = self.output_box.get(1.0, tk.END).strip()
        if textval:
            pyperclip.copy(textval)
            messagebox.showinfo("Copied", "Full prompt copied to clipboard.")

    def save_favorite(self):
        textval = self.output_box.get(1.0, tk.END).strip()
        if not textval:
            messagebox.showwarning("Empty", "No generated prompt to save.")
            return
        try:
            with open("wan22_favorites.txt", "a", encoding="utf-8") as fav:
                fav.write(textval + "\n\n")
            messagebox.showinfo("Saved", "Prompt appended to wan22_favorites.txt")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save: {e}")


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    app = Wan22PromptBuilderAppV2(WAN_PROMPTS_V2)
    app.mainloop()
