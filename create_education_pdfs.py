"""
Create multiple educational PDFs for comprehensive quiz testing
Covers various subjects: Math, Science, History, Literature, Computer Science
"""

import fitz  # PyMuPDF

def create_mathematics_pdf():
    """Create Mathematics PDF with algebra, geometry, and calculus content"""
    doc = fitz.open()
    page = doc.new_page()
    
    page.insert_text((50, 50), "Mathematics Fundamentals", fontsize=18, color=(0, 0, 0))
    
    content = """
Mathematics: The Language of Science

Algebra Fundamentals

Algebra is a branch of mathematics that uses symbols and letters to represent numbers and quantities in formulas and equations. The fundamental concept in algebra is the variable, typically represented by letters like x, y, or z.

Linear Equations:
A linear equation is an equation that makes a straight line when graphed. The standard form is y = mx + b, where:
- m is the slope (rate of change)
- b is the y-intercept (where the line crosses the y-axis)
- x is the independent variable
- y is the dependent variable

Quadratic Equations:
Quadratic equations have the form ax² + bx + c = 0, where a ≠ 0. These equations can be solved using:
- Factoring method
- Quadratic formula: x = (-b ± √(b² - 4ac)) / 2a
- Completing the square method

Geometry Principles

Geometry is the study of shapes, sizes, positions, angles, and dimensions of objects.

Basic Shapes and Properties:
- Triangle: A polygon with three sides. The sum of interior angles is always 180°
- Square: A quadrilateral with four equal sides and four right angles
- Circle: A round shape where all points are equidistant from the center
- Rectangle: A quadrilateral with opposite sides equal and four right angles

Pythagorean Theorem:
In a right triangle, the square of the hypotenuse equals the sum of squares of the other two sides: a² + b² = c²

Area Formulas:
- Triangle: Area = ½ × base × height
- Rectangle: Area = length × width
- Circle: Area = π × radius²
- Parallelogram: Area = base × height

Calculus Introduction

Calculus is the mathematical study of continuous change. It has two main branches:

Differential Calculus:
Studies rates of change and slopes of curves. The derivative of a function f(x) represents the instantaneous rate of change.

Basic derivative rules:
- Power rule: d/dx(xⁿ) = nxⁿ⁻¹
- Product rule: d/dx(uv) = u'v + uv'
- Chain rule: d/dx(f(g(x))) = f'(g(x)) × g'(x)

Integral Calculus:
Studies accumulation of quantities and areas under curves. Integration is the reverse process of differentiation.

Fundamental Theorem of Calculus:
If F(x) is an antiderivative of f(x), then ∫[a to b] f(x)dx = F(b) - F(a)

Statistics and Probability

Statistics is the science of collecting, analyzing, and interpreting data.

Measures of Central Tendency:
- Mean: The average of all values
- Median: The middle value when data is ordered
- Mode: The most frequently occurring value

Probability Basics:
Probability measures the likelihood of an event occurring, expressed as a number between 0 and 1.
- P(Event) = Number of favorable outcomes / Total number of possible outcomes
- Independent events: P(A and B) = P(A) × P(B)
- Mutually exclusive events: P(A or B) = P(A) + P(B)

Number Theory

Prime Numbers:
A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
Examples: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29...

Greatest Common Divisor (GCD):
The largest positive integer that divides both numbers without remainder.

Least Common Multiple (LCM):
The smallest positive integer that is divisible by both numbers.

Mathematical Problem Solving

Problem-solving strategies in mathematics:
1. Understand the problem
2. Devise a plan
3. Carry out the plan
4. Look back and check

Common problem-solving techniques:
- Draw a diagram or picture
- Make a table or chart
- Look for patterns
- Work backwards
- Guess and check
- Use logical reasoning

Applications of Mathematics:
- Engineering: Structural design, electrical circuits
- Physics: Motion, forces, energy calculations
- Economics: Market analysis, financial modeling
- Computer Science: Algorithms, data structures
- Biology: Population growth, genetic modeling
"""
    
    text_rect = fitz.Rect(50, 80, 550, 750)
    page.insert_textbox(text_rect, content, fontsize=10, color=(0, 0, 0))
    
    filename = "Mathematics_Fundamentals.pdf"
    doc.save(filename)
    doc.close()
    return filename

def create_science_pdf():
    """Create Science PDF with physics, chemistry, and biology content"""
    doc = fitz.open()
    page = doc.new_page()
    
    page.insert_text((50, 50), "Science Fundamentals", fontsize=18, color=(0, 0, 0))
    
    content = """
Science: Understanding the Natural World

Physics Principles

Physics is the fundamental science that seeks to understand how the universe works.

Newton's Laws of Motion:
1. First Law (Inertia): An object at rest stays at rest, and an object in motion stays in motion, unless acted upon by an external force.
2. Second Law: Force equals mass times acceleration (F = ma)
3. Third Law: For every action, there is an equal and opposite reaction.

Energy and Work:
- Kinetic Energy: Energy of motion, KE = ½mv²
- Potential Energy: Stored energy, PE = mgh (gravitational)
- Work: Force applied over a distance, W = F × d
- Conservation of Energy: Energy cannot be created or destroyed, only transformed

Waves and Sound:
- Wave properties: frequency, wavelength, amplitude
- Sound travels through vibrations in matter
- Speed of sound in air: approximately 343 m/s at room temperature

Electricity and Magnetism:
- Electric current: flow of electric charge
- Ohm's Law: V = IR (Voltage = Current × Resistance)
- Magnetic fields are created by moving electric charges

Chemistry Fundamentals

Chemistry studies the composition, structure, and properties of matter.

Atomic Structure:
- Atoms consist of protons, neutrons, and electrons
- Protons have positive charge, electrons negative, neutrons neutral
- Atomic number = number of protons
- Mass number = protons + neutrons

Periodic Table:
- Elements arranged by atomic number
- Groups (columns) have similar properties
- Periods (rows) show electron shell patterns
- Metals, nonmetals, and metalloids

Chemical Bonds:
- Ionic bonds: transfer of electrons between atoms
- Covalent bonds: sharing of electrons between atoms
- Metallic bonds: sea of electrons in metal structures

Chemical Reactions:
- Reactants → Products
- Conservation of mass: atoms are neither created nor destroyed
- Types: synthesis, decomposition, single/double replacement

States of Matter:
- Solid: fixed shape and volume, particles vibrate in place
- Liquid: fixed volume, variable shape, particles move freely
- Gas: variable shape and volume, particles move rapidly
- Plasma: ionized gas at very high temperatures

Biology Essentials

Biology is the study of living organisms and life processes.

Cell Theory:
1. All living things are made of cells
2. Cells are the basic unit of life
3. All cells come from pre-existing cells

Cell Structure:
- Prokaryotic cells: no nucleus (bacteria)
- Eukaryotic cells: have nucleus (plants, animals, fungi)
- Organelles: specialized structures within cells

DNA and Genetics:
- DNA contains genetic information in sequences of bases (A, T, G, C)
- Genes are segments of DNA that code for traits
- Chromosomes carry genes
- Heredity: traits passed from parents to offspring

Evolution:
- Natural selection: survival of the fittest
- Adaptation: traits that help organisms survive
- Species change over time through genetic variation
- Common descent: all life shares common ancestors

Ecosystems:
- Food chains and food webs show energy flow
- Producers (plants) convert sunlight to energy
- Consumers eat other organisms for energy
- Decomposers break down dead material

Human Body Systems:
- Circulatory: heart and blood vessels transport materials
- Respiratory: lungs exchange oxygen and carbon dioxide
- Digestive: breaks down food for nutrients
- Nervous: brain and nerves control body functions

Scientific Method

The scientific method is a systematic approach to understanding the natural world:

1. Observation: Notice something in the natural world
2. Question: Ask a specific question about the observation
3. Hypothesis: Propose a testable explanation
4. Experiment: Design and conduct tests
5. Analysis: Examine the data collected
6. Conclusion: Determine if hypothesis is supported
7. Communication: Share results with others

Variables in Experiments:
- Independent variable: what you change
- Dependent variable: what you measure
- Control variables: what you keep the same
- Control group: baseline for comparison

Environmental Science

Environmental science studies interactions between physical, chemical, and biological components of the environment.

Climate Change:
- Greenhouse effect: gases trap heat in atmosphere
- Global warming: increase in Earth's average temperature
- Causes: burning fossil fuels, deforestation
- Effects: rising sea levels, changing weather patterns

Pollution Types:
- Air pollution: harmful substances in atmosphere
- Water pollution: contamination of water bodies
- Soil pollution: contamination of land
- Noise pollution: excessive sound levels

Conservation:
- Renewable resources: can be replenished naturally
- Non-renewable resources: finite supply
- Sustainability: meeting present needs without compromising future
- Biodiversity: variety of life in ecosystems
"""
    
    text_rect = fitz.Rect(50, 80, 550, 750)
    page.insert_textbox(text_rect, content, fontsize=10, color=(0, 0, 0))
    
    filename = "Science_Fundamentals.pdf"
    doc.save(filename)
    doc.close()
    return filename

def create_history_pdf():
    """Create History PDF with world history and important events"""
    doc = fitz.open()
    page = doc.new_page()
    
    page.insert_text((50, 50), "World History Overview", fontsize=18, color=(0, 0, 0))
    
    content = """
World History: Understanding Our Past

Ancient Civilizations

Mesopotamia (3500-539 BCE):
- Located between Tigris and Euphrates rivers
- Developed first writing system (cuneiform)
- Created the wheel and first cities
- Hammurabi's Code: one of first written law codes

Ancient Egypt (3100-30 BCE):
- Developed along the Nile River
- Built pyramids and sphinx monuments
- Created hieroglyphic writing system
- Advanced medicine and mathematics
- Pharaohs ruled as god-kings

Ancient Greece (800-146 BCE):
- Birthplace of democracy in Athens
- Philosophy: Socrates, Plato, Aristotle
- Olympic Games originated here
- Alexander the Great spread Greek culture
- Contributions to art, science, and politics

Roman Empire (27 BCE-476 CE):
- Vast empire spanning Europe, Africa, Asia
- Roman law influenced modern legal systems
- Built extensive road networks and aqueducts
- Latin language spread throughout empire
- Christianity became official religion under Constantine

Medieval Period (476-1453 CE)

Feudalism:
- Social system based on land ownership
- Lords granted land to vassals for military service
- Serfs worked the land for protection
- Castles provided defense and administration

The Crusades (1095-1291):
- Religious wars between Christians and Muslims
- Fought for control of Holy Land
- Increased trade between Europe and Asia
- Cultural exchange of ideas and technology

Black Death (1347-1351):
- Bubonic plague killed 1/3 of Europe's population
- Spread along trade routes from Asia
- Led to social and economic changes
- Weakened feudal system

Renaissance (1400-1600)

Characteristics:
- "Rebirth" of classical learning and culture
- Humanism: focus on human potential and achievement
- Scientific revolution and artistic innovation
- Printing press spread knowledge rapidly

Key Figures:
- Leonardo da Vinci: artist, inventor, scientist
- Michelangelo: sculptor and painter
- Galileo Galilei: astronomer and physicist
- William Shakespeare: playwright and poet

Age of Exploration (1400-1600):
- Europeans explored and colonized new lands
- Christopher Columbus reached Americas (1492)
- Vasco da Gama sailed to India
- Magellan's expedition circumnavigated globe

Industrial Revolution (1760-1840)

Causes:
- Agricultural improvements freed workers
- Natural resources (coal, iron) available
- Capital for investment accumulated
- Transportation improvements

Key Inventions:
- Steam engine powered factories and transportation
- Textile machinery increased production
- Railroad networks connected markets
- Telegraph improved communication

Social Changes:
- Urbanization: people moved to cities
- Factory system replaced home production
- New social classes emerged
- Working conditions often poor

Modern Era (1800-Present)

World War I (1914-1918):
- "The Great War" involved major world powers
- Trench warfare on Western Front
- New weapons: machine guns, poison gas, tanks
- Russian Revolution occurred during war
- Treaty of Versailles ended war

World War II (1939-1945):
- Axis powers (Germany, Italy, Japan) vs. Allies
- Holocaust: systematic murder of 6 million Jews
- Nuclear weapons used on Japan
- United Nations formed after war
- Beginning of Cold War

Cold War (1947-1991):
- Ideological conflict between US and Soviet Union
- Nuclear arms race and space race
- Berlin Wall divided East and West Germany
- Korean War and Vietnam War
- Ended with fall of Soviet Union

Decolonization:
- European colonies gained independence
- India and Pakistan independence (1947)
- African nations gained freedom (1950s-1960s)
- End of European empires

Civil Rights Movement:
- Fight for equal rights for African Americans
- Martin Luther King Jr. led peaceful protests
- Brown v. Board ended school segregation
- Civil Rights Act (1964) banned discrimination

Technological Revolution:
- Computer age began in late 20th century
- Internet connected the world
- Mobile technology transformed communication
- Social media changed how people interact

Historical Thinking Skills

Analyzing Primary Sources:
- Documents, artifacts, images from the time period
- Consider author's perspective and bias
- Understand historical context
- Compare multiple sources

Cause and Effect:
- Identify factors that led to historical events
- Understand short-term and long-term consequences
- Recognize multiple causes for complex events

Change and Continuity:
- What changed over time?
- What remained the same?
- How fast did changes occur?
- What factors promoted or hindered change?

Historical Significance:
- Why do certain events matter?
- How did they affect people at the time?
- What long-term impact did they have?
- How do they connect to present day?
"""
    
    text_rect = fitz.Rect(50, 80, 550, 750)
    page.insert_textbox(text_rect, content, fontsize=10, color=(0, 0, 0))
    
    filename = "World_History_Overview.pdf"
    doc.save(filename)
    doc.close()
    return filename

def create_literature_pdf():
    """Create Literature PDF with literary analysis and major works"""
    doc = fitz.open()
    page = doc.new_page()
    
    page.insert_text((50, 50), "Literature and Language Arts", fontsize=18, color=(0, 0, 0))
    
    content = """
Literature and Language Arts

Literary Elements and Devices

Plot Structure:
- Exposition: introduces characters and setting
- Rising Action: conflict develops and tension builds
- Climax: turning point or highest tension
- Falling Action: events after climax
- Resolution: conflict is resolved

Character Types:
- Protagonist: main character
- Antagonist: opposes the protagonist
- Round characters: complex and well-developed
- Flat characters: simple, one-dimensional
- Dynamic characters: change throughout story
- Static characters: remain unchanged

Setting:
- Time: when the story takes place
- Place: where the story occurs
- Atmosphere: mood created by setting
- Historical context: social and cultural background

Theme:
- Central message or meaning of the work
- Universal truths about human experience
- Often implied rather than directly stated
- Can have multiple themes in one work

Literary Devices:
- Metaphor: direct comparison without "like" or "as"
- Simile: comparison using "like" or "as"
- Symbolism: objects represent deeper meanings
- Irony: contrast between expectation and reality
- Foreshadowing: hints about future events
- Alliteration: repetition of initial consonant sounds

Poetry Analysis

Poetic Forms:
- Sonnet: 14-line poem with specific rhyme scheme
- Haiku: 3-line Japanese poem (5-7-5 syllables)
- Free verse: no regular pattern or rhyme
- Ballad: narrative poem often set to music

Sound Devices:
- Rhyme: matching sounds at end of lines
- Rhythm: pattern of stressed and unstressed syllables
- Meter: regular pattern of rhythm
- Assonance: repetition of vowel sounds
- Consonance: repetition of consonant sounds

Figurative Language:
- Personification: giving human qualities to non-human things
- Hyperbole: deliberate exaggeration
- Onomatopoeia: words that imitate sounds
- Allusion: reference to another work or historical event

Major Literary Periods

Classical Literature:
- Ancient Greek and Roman works
- Homer's "Iliad" and "Odyssey"
- Greek tragedies by Sophocles and Euripides
- Established many literary conventions

Medieval Literature:
- Religious themes dominated
- "Beowulf": Anglo-Saxon epic poem
- Dante's "Divine Comedy"
- Chaucer's "Canterbury Tales"

Renaissance Literature:
- Humanism and individualism themes
- William Shakespeare: greatest English playwright
- "Romeo and Juliet," "Hamlet," "Macbeth"
- Sonnets and complex characters

Romantic Period (1800-1850):
- Emphasis on emotion and nature
- William Wordsworth and Samuel Coleridge
- Lord Byron and Percy Shelley
- Focus on individual experience

Victorian Literature (1837-1901):
- Social criticism and moral issues
- Charles Dickens: "Oliver Twist," "Great Expectations"
- Charlotte Brontë: "Jane Eyre"
- Realistic portrayal of society

Modern Literature (1900-1945):
- Experimental forms and techniques
- Stream of consciousness narrative
- T.S. Eliot: "The Waste Land"
- James Joyce: "Ulysses"

Contemporary Literature (1945-present):
- Diverse voices and perspectives
- Postmodern techniques
- Multicultural themes
- Digital age influences

Reading Comprehension Strategies

Active Reading:
- Preview text before reading
- Ask questions while reading
- Make predictions about what will happen
- Visualize scenes and characters
- Summarize main points

Critical Analysis:
- Identify author's purpose
- Analyze character motivations
- Examine cause and effect relationships
- Compare and contrast elements
- Evaluate author's effectiveness

Context Clues:
- Definition: meaning given in text
- Example: specific instances provided
- Synonym: similar word used nearby
- Antonym: opposite word suggests meaning
- Inference: logical conclusion from evidence

Writing Process

Pre-writing:
- Brainstorming ideas
- Organizing thoughts
- Creating outlines
- Researching topics

Drafting:
- Writing first version
- Focus on getting ideas down
- Don't worry about perfection
- Include introduction, body, conclusion

Revising:
- Improve content and organization
- Add, delete, or rearrange ideas
- Strengthen arguments
- Clarify confusing passages

Editing:
- Correct grammar and spelling
- Fix punctuation errors
- Improve sentence structure
- Check word choice

Publishing:
- Prepare final version
- Share with intended audience
- Consider format and presentation

Essay Types:
- Narrative: tells a story
- Descriptive: creates vivid picture
- Expository: explains or informs
- Persuasive: argues a position
- Compare/contrast: examines similarities and differences

Grammar and Language

Parts of Speech:
- Noun: person, place, thing, or idea
- Pronoun: replaces a noun
- Verb: action or state of being
- Adjective: describes a noun
- Adverb: describes a verb, adjective, or adverb
- Preposition: shows relationship between words
- Conjunction: connects words or phrases
- Interjection: expresses emotion

Sentence Structure:
- Simple: one independent clause
- Compound: two independent clauses joined
- Complex: independent clause with dependent clause
- Compound-complex: multiple independent and dependent clauses

Punctuation Rules:
- Period: ends declarative sentences
- Question mark: ends interrogative sentences
- Exclamation point: shows strong emotion
- Comma: separates elements in a series
- Semicolon: joins related independent clauses
- Colon: introduces lists or explanations
"""
    
    text_rect = fitz.Rect(50, 80, 550, 750)
    page.insert_textbox(text_rect, content, fontsize=10, color=(0, 0, 0))
    
    filename = "Literature_Language_Arts.pdf"
    doc.save(filename)
    doc.close()
    return filename

def create_computer_science_pdf():
    """Create Computer Science PDF with programming and technology concepts"""
    doc = fitz.open()
    page = doc.new_page()
    
    page.insert_text((50, 50), "Computer Science Fundamentals", fontsize=18, color=(0, 0, 0))
    
    content = """
Computer Science: The Digital Age

Programming Fundamentals

What is Programming?
Programming is the process of creating instructions for computers to follow. These instructions, called code, tell the computer how to perform specific tasks.

Programming Languages:
- Python: Easy to learn, versatile, great for beginners
- Java: Object-oriented, platform-independent
- C++: Powerful, used for system programming
- JavaScript: Essential for web development
- HTML/CSS: Markup and styling for web pages

Basic Programming Concepts:
- Variables: store data values
- Data types: integers, strings, booleans, floats
- Operators: arithmetic (+, -, *, /), comparison (==, !=, <, >)
- Control structures: if/else statements, loops
- Functions: reusable blocks of code
- Arrays/Lists: collections of data

Algorithms and Problem Solving:
- Algorithm: step-by-step procedure to solve a problem
- Pseudocode: plain language description of algorithm
- Flowcharts: visual representation of algorithm steps
- Debugging: finding and fixing errors in code

Data Structures:
- Arrays: ordered collection of elements
- Linked Lists: elements connected by pointers
- Stacks: Last In, First Out (LIFO) structure
- Queues: First In, First Out (FIFO) structure
- Trees: hierarchical data structure
- Hash Tables: key-value pair storage

Computer Systems and Hardware

Computer Components:
- CPU (Central Processing Unit): executes instructions
- RAM (Random Access Memory): temporary storage
- Storage: hard drives, SSDs for permanent data
- Input devices: keyboard, mouse, touchscreen
- Output devices: monitor, printer, speakers

Binary System:
- Computers use binary (base-2) number system
- Only two digits: 0 and 1
- Each digit is called a bit
- 8 bits make a byte
- Used to represent all data and instructions

Operating Systems:
- Software that manages computer hardware
- Examples: Windows, macOS, Linux, Android, iOS
- Functions: file management, memory allocation, security
- User interface: command line or graphical

Networks and Internet:
- Network: connected computers sharing resources
- Internet: global network of networks
- Protocols: rules for communication (HTTP, TCP/IP)
- World Wide Web: system of linked documents

Software Development

Software Development Life Cycle (SDLC):
1. Planning: define project scope and requirements
2. Analysis: study existing systems and needs
3. Design: create system architecture and interface
4. Implementation: write and test code
5. Testing: verify software works correctly
6. Deployment: release software to users
7. Maintenance: ongoing support and updates

Programming Paradigms:
- Procedural: step-by-step instructions
- Object-Oriented: code organized into objects
- Functional: functions as primary building blocks
- Event-Driven: responds to user actions

Version Control:
- Git: tracks changes in code over time
- Repositories: storage for project files
- Commits: saved snapshots of code
- Branches: parallel development paths
- Collaboration: multiple developers working together

Database Management

What are Databases?
Databases store and organize large amounts of information for easy retrieval and manipulation.

Database Types:
- Relational: data stored in tables with relationships
- NoSQL: flexible structure for unstructured data
- Graph: data represented as nodes and connections
- Document: stores data as documents (JSON, XML)

SQL (Structured Query Language):
- Standard language for relational databases
- SELECT: retrieve data from tables
- INSERT: add new data
- UPDATE: modify existing data
- DELETE: remove data
- JOIN: combine data from multiple tables

Database Design:
- Tables: organize data into rows and columns
- Primary Key: unique identifier for each row
- Foreign Key: links tables together
- Normalization: reduce data redundancy
- Indexes: improve query performance

Cybersecurity

Information Security Principles:
- Confidentiality: protect data from unauthorized access
- Integrity: ensure data accuracy and completeness
- Availability: systems accessible when needed

Common Threats:
- Malware: viruses, worms, trojans, ransomware
- Phishing: fraudulent emails to steal information
- Social Engineering: manipulating people for information
- DDoS attacks: overwhelming systems with traffic
- Data breaches: unauthorized access to sensitive data

Security Measures:
- Passwords: strong, unique for each account
- Two-factor authentication: additional security layer
- Encryption: scrambling data to protect it
- Firewalls: filter network traffic
- Antivirus software: detect and remove malware
- Regular updates: patch security vulnerabilities

Artificial Intelligence and Machine Learning

Artificial Intelligence (AI):
- Computer systems that can perform tasks requiring human intelligence
- Applications: speech recognition, image processing, game playing
- Types: narrow AI (specific tasks) vs. general AI (human-level)

Machine Learning:
- Subset of AI where computers learn from data
- Supervised learning: learns from labeled examples
- Unsupervised learning: finds patterns in unlabeled data
- Reinforcement learning: learns through trial and error

Applications:
- Recommendation systems (Netflix, Amazon)
- Image recognition (photo tagging, medical diagnosis)
- Natural language processing (chatbots, translation)
- Autonomous vehicles (self-driving cars)
- Predictive analytics (weather, stock market)

Web Development

Frontend Development:
- HTML: structure and content of web pages
- CSS: styling and layout
- JavaScript: interactivity and dynamic behavior
- Responsive design: works on all device sizes
- User experience (UX): how users interact with site

Backend Development:
- Server-side programming: Python, Java, PHP, Node.js
- Databases: store and retrieve data
- APIs: allow different systems to communicate
- Security: protect user data and prevent attacks
- Performance: optimize speed and efficiency

Web Technologies:
- HTTP/HTTPS: protocols for web communication
- DNS: translates domain names to IP addresses
- CDN: content delivery networks for faster loading
- Cloud computing: remote servers and services

Ethics in Technology

Digital Divide:
- Gap between those with and without technology access
- Affects education, employment, and social opportunities
- Solutions: public internet access, affordable devices

Privacy Concerns:
- Data collection by companies and governments
- Personal information used for advertising
- Surveillance and tracking technologies
- Right to privacy vs. security needs

Intellectual Property:
- Copyright: protects creative works
- Patents: protect inventions and processes
- Open source: freely available software
- Fair use: limited use of copyrighted material

Future of Computing:
- Quantum computing: exponentially faster processing
- Internet of Things (IoT): connected everyday objects
- Augmented/Virtual Reality: immersive experiences
- Blockchain: decentralized and secure transactions
"""
    
    text_rect = fitz.Rect(50, 80, 550, 750)
    page.insert_textbox(text_rect, content, fontsize=10, color=(0, 0, 0))
    
    filename = "Computer_Science_Fundamentals.pdf"
    doc.save(filename)
    doc.close()
    return filename

def main():
    """Create all educational PDFs"""
    print("🎓 Creating Educational PDFs for Quiz Generation...")
    print("=" * 60)
    
    created_files = []
    
    # Create each subject PDF
    subjects = [
        ("Mathematics", create_mathematics_pdf),
        ("Science", create_science_pdf),
        ("History", create_history_pdf),
        ("Literature", create_literature_pdf),
        ("Computer Science", create_computer_science_pdf)
    ]
    
    for subject_name, create_func in subjects:
        try:
            filename = create_func()
            created_files.append(filename)
            print(f"✅ Created: {filename}")
        except Exception as e:
            print(f"❌ Error creating {subject_name} PDF: {e}")
    
    print("\n" + "=" * 60)
    print(f"🎉 Successfully created {len(created_files)} educational PDFs!")
    print("\n📚 Available subjects for quiz generation:")
    
    for i, filename in enumerate(created_files, 1):
        subject = filename.replace("_", " ").replace(".pdf", "")
        print(f"{i}. {subject}")
    
    print("\n🎯 Perfect for testing automatic quiz generation!")
    print("📝 Each PDF contains comprehensive educational content")
    print("🤖 AI will generate relevant multiple-choice questions")
    print("✅ Upload these PDFs to StudyMate and create quizzes!")

if __name__ == "__main__":
    main()
