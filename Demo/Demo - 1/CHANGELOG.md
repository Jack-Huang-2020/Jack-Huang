### **Whimscape 1.20.2-1.21.5_r3** (2025 May 20)
- added paintings 'pond' and 'sunflowers'
- added item sprites for boats, minecarts, lanterns, comparator, repeater, brewing stand, amethyst buds/cluster, pointed dripstone and iron bars (1.21.4+)
    - held and dropped items are still shown as 3D models
    - in game versions before 1.21.4, the 3D models are still shown in every display context
- added GUI textures: tab and text field widgets
- added entity textures: happy ghast and ghastling
- added dormant creaking heart block textures (1.21.5+)
- added light_emission fields to many block model elements, replacing OptiFine/Continuity emissive textures (1.21.2+)
- added soul lantern emissive texture for OptiFine/Continuity (1.20.2-1.21.1)
- added waxed block item textures with a glint animation
- fixed EMI mod support: added a missing sprite to widgets.png
- fixed active/awake creaking heart block texture (1.21.5+)
- changed GUI:
    - button disabled textures
    - header and footer separator textures
    - gui\sprites\trial_available texture
- changed block and item models:
    - brewing stand bottles
    - amethyst buds/cluster display tweaks
    - lantern display tweaks
    - replaced negative-sized elements in cauldrons, hoppers, open barrel, outlined blocks
    - moved shield idle position in first person view to be even less in the way and better match its third person position
    - waxed blocks: removed outline from items
- changed block textures:
    - brewing stand bottles
    - end portal frame eye
    - heavy core: changed top and bottom
    - lantern emissive texture tweak for OptiFine/Continuity (1.20.2-1.21.1)
    - sunflower
    - torch flame animations
    - composter/note block/jukebox/pitcher crop/scaffolding top: slight tweak to a single color
- changed item textures:
    - chorus fruits
    - cookie
    - buckets
    - ominous bottle
    - sunflower
    - torch flame animations
    - tiny tweaks to some other items
- changed entities: tweaks to cow, ghast, shield and slime textures
- changed paintings 'earth', 'wind', 'fire' and 'water'
- removed unused cauldron block models


### **Whimscape 1.20.2-1.21.5_r2** (2025 Apr 20)
- added mod support: TrashSlot
- added bogged custom entity model with 3D mushrooms
- added grass block models to only rotate the top texture
- added bamboo gate models, fixed the texture
- added variants of axolotl bucket item for 1.21.5 (no CIT needed)
- added CIT for enchanted books breach, density and wind burst in 1.20.5+
- added animation to campfire item textures
- fixed missing, redundant or wrong texture and parent references in many models
- fixed warnings about unused frames in conduit wind sprites: cropped out unused frames
- fixed small textures in the Waystones mod limiting mip level from 4 to 3
- fixed CIT for axolotl buckets in 1.20.5-1.21.4
- fixed CIT for sweeping edge enchanted book in 1.20.5+
- fixed warm chicken baby and warm pig showing up as temperate variants when using EMF custom models
- changed all pig variants' custom models and textures
- changed slime entity texture slightly (in previous release, missed from changelog)
- changed conduit wind animation frametime from 3 to 1
- changed fence and gate models: separated from default templates for mod compatibility
- changed item textures: all books and smithing templates, spider eyes, egg, gold ingot
- removed unmodified texture moss_template.png in Waystones mod assets
- removed mod support: dorianpb's Custom Entity Models


### **Whimscape 1.20.2-1.21.5_r1** (2025 Apr 12)
- added mod support: Waystones
- added 'bouquet' and 'cavebird' paintings
- added block and item textures for bush, cactus flower, dry grasses, firefly bush, leaf litter, wildflowers
- added cold and warm variants for chicken, cow and pig
- added sheep wool and undercoat textures
- added blue and brown egg item textures
- added leaf particle textures
- added firefly particle texture
- added cherry leaves variant texture
- fixed mooshrooms and temperate cow/pig/chicken for 1.21.5
- fixed armor enchantment glint for 1.21.5
- fixed entity saddle textures for 1.21.5
- fixed textures\gui\sprites\container\slot.png to better match the GUI panels that use it
- fixed Fabric creative inventory page button texture for 1.21.1, 1.21.4, 1.21.5
- changed chicken texture
- changed pig texture and custom model
- changed lodestone side texture for 1.21.5 to match the new crafting recipe
- changed egg item texture
- changed pufferfish item texture colors slightly
- changed dead bush block texture slightly
- changed cherry leaves texture slightly
- changed donkey, mule and zombie horse spawn egg textures: 1-pixel tweak


### **Whimscape 1.20.2-1.21.4_r2** (2024 Dec 21)
- added tuff brick wall and polished tuff wall models and textures
- added matching inventory models for wall blocks with custom texture mapping
- added slot highlight background texture
- fixed clock item for 1.21.4
- fixed wolf armor head tilting on its own
- changed closed eyeblossom block and item textures slightly
- removed textures\block\sand_s.png
- removed blockstates\resin_brick_wall.json


### **Whimscape 1.20.2-1.21.4_r1** (2024 Dec 3)
- added creaking entity textures
- added resin block, resin clump, resin bricks and chiseled resin bricks block textures
- added resin brick wall models and textures
- added resin brick and resin clump item textures
- added pale oak leaf particle textures
- added eyeblossom block and item textures
- added resin trim palette
- added 'tides' painting
- fixed magma cube texture for 1.21.4
- fixed spawn eggs for 1.21.4
- fixed infested and waxed block items for 1.21.4
- fixed gui sprites for 1.21.4: empty slots, toast/system, toast/tutorial, advancements/box_obtained, advancements/box_unobtained
- fixed two pixels in the bolt armor trim not matching the trim palette
- changed pale oak door and sign item colors slightly
- changed active creaking heart textures: color tweak
- changed chestplate armor trim item overlay slightly
- changed spawn eggs: tweaks to creaking, mooshroom and witch


### **Whimscape 1.20.2-1.21.3_r1** (2024 Oct 26)
- added pale oak wood set textures and models
- added pale moss textures and models
- added pale oak log and leaf textures
- added pale oak sapling textures and models
- added creaking heart textures
- added creaking spawn egg
- added bordure indented and field masoned banner pattern item textures
- added empty air bubble hud texture
- added mod support: Dungeons and Taverns key item textures
- added mod support: Visuality particle textures
- added mod support: Mod Menu GUI textures
- added mod support: oωo library GUI textures
- added mod support: Entity Features config button textures
- added mod support: Roughly Enough Items (REI)
- added mod support: EMI
- added mod support: Fabric creative inventory page buttons texture
- added missing Just Enough Items (JEI) textures
- fixed errant pixel in fox and wolf spawn egg items
- fixed tropical fish fin patterns being one-sided
- changed some GUI elements
- changed f, G, i, J, j, t, y and some cyrillic glyphs of the font
- changed enchanted glint textures
- changed many spawn egg items slightly
- changed acacia leaves color slightly
- changed grass and fern base texture colors: reduced saturation of darker shades
- changed banner pattern item textures


### **Whimscape 1.20.2-1.21.1_r1** (2024 Sep 30)
- added painting textures: baroque, changing, meditative, prairie_ride, unpacked
- added bundle variant textures
- added bundle GUI textures
- added tooltip textures
- added missing torch template block models
- added comparator and repeater models (from 24w38a with UV tweaks)
- added textures for comparator block's subtraction mode
- fixed equipment model texture locations in pack_format 37+
- fixed bundle textures in pack_format 35+
- fixed arrow & bee stinger entity textures in pack_format 35+
- changed wall torch block model slightly
- changed redstone torch block and item textures
- changed comparator and repeater textures slightly
- changed pitcher plant item texture slightly
- changed bee spawn egg item texture: 1-pixel tweak
- changed the colors of brown dye and brown candle item textures


### **Whimscape 1.20.2-1.21_r2** (2024 Jul 10)
- added bogged entity textures
- added bogged spawn egg texture
- added status effect icons: infested, oozing, weaving, wind_charged
- added particle textures: infested, ominous_spawning, raid_omen, small_gust, trial_omen, trial_spawner_detection_ominous, vault_connection
- added painting texture: humble
- fixed moss carpet sides being fully opaque in 1.21
- changed wind charge item texture
- changed gust particle colors
- changed wind charge projectile colors


### **Whimscape 1.20.2-1.21_r1** (2024 Jun 15)
- added mace, ominous bottle, ominous trial key, wind charge item textures
- added music discs: creator, creator (music box), precipice
- added vault, ominous vault, ominous trial spawner textures
- added bolt and flow armor trim textures
- added raid omen and trial omen effect icons
- fixed copper bulb texture names for the lit & powered state
- changed trial spawner textures
- changed trial key texture
- changed bad omen effect icon for 1.21
- changed crafter north face and weathered copper bulbs: 2-pixel tweaks


### **Whimscape 1.20.2-1.20.5_r1** (2024 Apr 24)
- added wolf variant textures
- added wolf armor overlay and crackiness textures
- added spawn egg textures for armadillo and breeze
- added breeze rod texture
- added flow and bolt smithing template textures
- added flow and guster banner and shield patterns
- added flow, guster and scrape pottery textures
- added gui inworld_footer_separator, inworld_header_separator, inworld_menu_background
- added gui/sprites/widget/scroller_background
- added trial_chambers map icon
- fixed map icons for resource pack format 30
- changed wolf textures: original wolf is now a lighter color
- changed pitcher plant colors
- changed sea lantern texture
- changed guardian and elder guardian textures


### **Whimscape 1.20.2-1.20.4_r2** (2024 Mar 19)
- added custom textures for spawn egg items
- added support for the AppleSkin mod
- added support for the Just Enough Items mod
- added support for the Farmer's Delight mod
- added wall torch model with a holder
- fixed menu gui elements for resource pack format 28
- fixed wind charge projectile texture
- fixed dolphin flipper texture orientation
- changed buttons & sliders to a simpler design
- changed recipe book craftable toggles slightly
- changed food hud icons: made smaller to allow for a clean outline in AppleSkin
- changed fuel progress textures: cleaner look
- changed pumpkins: clean up and color adjustment
- changed bee nest: partial redesign
- changed honeycomb block and beehive: adjusted honey color
- changed beetroots and potatoes: shading tweak on the tuber part
- changed crimson and warped stem tops: made distinct from regular logs
- changed cake block slightly
- changed mossy stone brick wall tops slightly
- changed brewing stand rod texture, added emissive map
- changed vindicator pants color
- changed farmland textures slightly
- changed pumpkin pie item: slight color adjustment
- changed potions, experience bottle, dragon's breath: tweaked bottle highlight
- changed stone axe, stone hoe, stone shovel, wooden shovel and wooden axe slightly
- changed cookie texture: made smaller
- changed mutton and cooked mutton texture
- changed bowl, stew and soup textures
- changed bone and bone meal texture colors slightly


### **Whimscape 1.20.2-1.20.4_r1** (2023 Dec 20)
- added gust particle textures
- added wind charge texture
- added armadillo texture
- added armadillo scute texture
- added wolf armor textures
- fixed turtle scute item texture name for snapshot 23w51a
- fixed breeze eyes for snapshot 23w51a
- changed the font's ampersand closer to the modern form
- changed potion textures
- changed dragon's breath texture
- changed experience bottle texture
- changed honey bottle texture
- changed flower pot item texture
- changed goat horn texture


### **Whimscape 1.20.2-1.20.3_r1** (2023 Dec 5)
- added models & textures for the new experimental features
- added darkness effect icon texture
- added textures\gui\sprites\widget\slot_frame.png
- fixed bat texture for the new model in 1.20.3
- fixed short grass in 1.20.3
- fixed waxed slab outline missing down-facing texture
- fixed button block textures being flipped vertically
- changed infested/waxed blocks: made item outline slightly thinner
- changed raw copper block texture slightly
- changed tuff colors slightly
- removed leftover realms folder


### **Whimscape 1.20.2_r1** (2023 Sep 26)
- added the new icons in map_icons.png
- fixed the GUI for 1.20.2
- changed structure_block_load, structure_block_save textures
- changed rail item outlines slightly
- changed gold ingot, copper ingot for slightly better distinction
- changed pack_format to 18

________________________________________________________________

### **Whimscape 1.20_r3** (2023 Jun 16)
- added paintings: earth, fire, water, wind
- fixed pot patterns: missing "plenty" pattern, wrong "prize" texture


### **Whimscape 1.20_r2** (2023 Jun 11)
- fixed OptiFine applying a tint to cherry leaves
- fixed some sniffer egg stage inconsistencies
- changed jungle door and trapdoor design
- changed iron door slightly to be able to tell which side it is on
- changed some other doors: minor tweaks


### **Whimscape 1.20_r1** (2023 Jun 7)
- added sniffer and sniffer egg textures
- added pitcher plant and torchflower blocks and items
- added armor trims and templates: host, raiser, shaper, silence, wayfinder
- added decorated pot textures
- added item textures: brush, pottery sherds, relic music disc
- added suspicious gravel
- added calibrated sculk sensor model and textures
- fixed menu logos and invite_icon for the new texture layouts in 1.20
- changed armor trims: dune, sentry
- changed some smithing templates
- changed cherry particles
- changed suspicious sand slightly
- changed bamboo and cherry doors, trapdoors
- changed bamboo block top texture
- changed pack_format to 15

________________________________________________________________

### **Whimscape 1.19.4_r1** (2023 Mar 15)
- added 1.20 data pack features: armor trims, cherry things, suspicious sand
- added world creation screen textures
- added the new separate gui/slider texture
- fixed smithing GUI textures, tweaked legacy gui
- changed some armor to work better with armor trims
- changed enchanted glint slightly
- changed pack_format to 13

________________________________________________________________

### **Whimscape 1.19.3_r8** (2023 Mar 12)
- added custom wither model, tweaked wither skull
- added a variant for sand and red sand
- added dorianpb/cem folder for the Fabric CEM mod, stripped out animations that break it
- fixed witch missing textures when using Fabric CEM
- fixed slight color inconsistency in empty armor slot textures
- changed amethyst blocks to match the custom amethyst cluster model better
- changed some pink colors slightly, pink glazed terracotta pattern tweak
- changed anvil GUI: tweaked icon


### **Whimscape 1.19.3_r7** (2023 Feb 19)
- added 1.20 data pack features: bamboo stuff, chiseled bookshelf, hanging signs, camel
- fixed nether wart missing break particles
- fixed rogue pixel in kelp texture
- fixed missing pixels in angry bee with nectar custom model
- fixed z-fighting in fish fins
- changed bamboo stalk to match the new bamboo blocks a bit better
- changed wandering trader custom model: added 3D pouches
- changed pillager, witch, wolf, horse_creamy: small tweaks
- changed item frame backgrounds
- changed loom, smithing table and stonecutter slightly
- changed azalea blocks slightly
- changed netherite: colors, sword to match tools better
- changed ancient debris colors slightly
- changed many items: minor color adjustments


### **Whimscape 1.19.3_r6** (2023 Feb 5)
- added custom bee model
- added custom witch model
- added textures for different colors of axolotl bucket (CIT)
- added custom colors: fog.end, sky.end, map.stone, map.water, xp orb
- added a variant for obsidian
- added texture for wither's armor effect
- added emissive texture for strider's eyes
- fixed creative inventory alignment with tabs
- changed ore blocks: made different ores a bit more unique
- changed enderman, endermite
- changed many other mobs: small tweaks
- changed obsidian blocks and entities: mostly a color tweak
- changed many blocks: small tweaks, minor color adjustments
- changed minecart shading slightly
- changed minecart items to use the actual minecart texture
- changed a few item textures slightly
- changed some armors slightly
- changed main menu logo: minor color tweak


### **Whimscape 1.19.3_r5** (2023 Jan 15)
- added custom models for chorus flower and plant
- fixed mossy stone brick slabs and stairs not using variant textures
- fixed drowned flipped arm and leg
- fixed wolf collar z-fighting when custom entity models are enabled
- fixed glass pane CTM not connecting properly in corners
- changed glass and stained glass CTM: enabled innerSeams
- changed ice, packed ice and frosted ice textures, added variants
- changed lever texture
- changed hopper: can now tell its direction from above
- changed stonecutter textures
- changed smoker bottom texture
- changed various other blocks slightly
- changed entities: tweaks to many mobs
- changed pack.png: small tweak


### **Whimscape 1.19.3_r4** (2023 Jan 5)
- added custom models for pumpkin stems & melon stems
- fixed netherite armor (1.19.3 releases still had old textures)
- fixed inconsistency in door side UVs
- fixed custom door models causing a mod compatibility issue
- changed lectern textures slightly
- changed cactus bottom texture
- changed some green colors slightly
- removed some unused door model files


### **Whimscape 1.19.3_r3** (2022 Dec 23)
- added unique textures for enchanted books
    - requires OptiFine, Options/Video Settings/Quality/Custom Items: ON
- changed all book item textures slightly
- changed experience bottle & dragon's breath item textures: added glow outlines


### **Whimscape 1.19.3_r2** (2022 Dec 17)
- added CTM for glass, stained glass, glass pane and tinted glass
    - you can delete a block's folder in assets\minecraft\optifine\ctm if you prefer no CTM, or turn it off in video settings
- changed glass & tinted glass colors slightly
- changed nether gold ore slightly
- changed iron block, iron trapdoor slightly
- changed netherite colors (netherite block, ancient debris, lodestone)
- changed netherite armor: partial redesign for a more sinister feel
- changed various items (mostly slight color tweaks)


### **Whimscape 1.19.3_r1** (2022 Dec 7)
- added textures\gui\checkbox.png
- added textures\gui\report_button.png
- added an outline to waxed copper blocks in item form
- added jigsaw block textures
- fixed vex textures for the new model in 1.19.3
- fixed missing transparency in allay texture
- fixed creative inventory textures for 1.19.3
- fixed boat items' missing textures (atlases\blocks.json with boat directories)
- fixed inconsistency in top & bottom of door UVs
- changed colors of mangrove wood slightly
- changed colors of bookshelf contents slightly
- changed a pixel on stripped log top textures
- changed OptiFine fog0 colormap slightly
- changed pack_format to 12
- removed some unused model files

________________________________________________________________

### **Whimscape 1.19_r2** (2022 Oct 8)
- added CHANGELOG.md
- added missing toasts.png icons
- added missing stripped mangrove log textures
- changed colors of mangrove wood blocks to match boats & signs
- removed unused glowstone mcmeta file


### **Whimscape 1.19_r1** (2022 Sep 29)
- initial release
