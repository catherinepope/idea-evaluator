#!/usr/bin/env python3
"""
Idea Evaluation Script
Helps evaluate course/book ideas against 10 key criteria
"""

def get_rating(question):
    """Get a valid rating (1-10) for a given question."""
    while True:
        try:
            print(f"\n📝 {question}")
            rating = input("Rating (1-10): ").strip()
            
            # Convert to integer
            rating_int = int(rating)
            
            # Validate range
            if 1 <= rating_int <= 10:
                return rating_int
            else:
                print("❌ Please enter a number between 1 and 10.")
                
        except ValueError:
            print("❌ Please enter a valid number between 1 and 10.")

def main():
    """Main evaluation function."""
    print("🚀 Idea Evaluation Tool")
    print("=" * 40)
    print("Rate each criterion from 1-10 (where 10 is best)")
    
    # Define the evaluation questions
    questions = [
        "How excited are you about this idea? 😍",
        "What's your level of expertise? 🎓",
        "How confident are you that people want this? 🎯",
        "How straightforward would it be? ⚡",
        "How quickly could you complete this? ⏱️",
        "How strong is your unique angle or differentiation? 💎",
        "How relevant will this idea be in 5 years' time? 🔮",
        "How low-maintenance will this be? 🧘",
        "How well does this fit with your strategy? 🎯",
        "How many doors would this open to other opportunities? 🚪"
    ]
    
    # Collect ratings
    ratings = []
    total_score = 0
    
    for i, question in enumerate(questions, 1):
        print(f"\n📊 Question {i} of {len(questions)}")
        rating = get_rating(question)
        ratings.append(rating)
        total_score += rating
        
        # Show progress
        progress = "█" * i + "░" * (len(questions) - i)
        print(f"Progress: [{progress}] {i}/{len(questions)}")
    
    # Display results
    print("\n" + "=" * 50)
    print("🎉 EVALUATION COMPLETE!")
    print("=" * 50)
    
    print("\n📋 Your Ratings:")
    for i, (question, rating) in enumerate(zip(questions, ratings), 1):
        # Remove emoji from question for cleaner display
        clean_question = question.split(' 😍')[0].split(' 🎓')[0].split(' 🎯')[0].split(' ⚡')[0].split(' ⏱️')[0].split(' 💎')[0].split(' 🔮')[0].split(' 🧘')[0].split(' 🚪')[0]
        stars = "⭐" * rating
        print(f"{i:2d}. {clean_question}: {rating}/10 {stars}")
    
    print(f"\n🏆 TOTAL SCORE: {total_score}/100")
    
    # Provide interpretation
    if total_score >= 80:
        interpretation = "🔥 Excellent! This idea scores very highly - strong candidate for your next project!"
    elif total_score >= 70:
        interpretation = "✅ Good score! This idea has strong potential and is worth pursuing."
    elif total_score >= 60:
        interpretation = "🤔 Moderate score. Consider if you can improve weak areas or if passion overrides concerns."
    elif total_score >= 50:
        interpretation = "⚠️  Below average score. Might be worth reconsidering or significantly refining this idea."
    else:
        interpretation = "🛑 Low score. This idea may not be the best use of your limited time right now."
    
    print(f"\n💡 Interpretation: {interpretation}")
    
    # Ask if they want to evaluate another idea
    print(f"\n{'='*50}")
    while True:
        another = input("Would you like to evaluate another idea? (y/n): ").strip().lower()
        if another in ['y', 'yes']:
            print("\n" + "="*50)
            main()  # Recursive call for another evaluation
            break
        elif another in ['n', 'no']:
            print("\n👋 Thanks for using the Idea Evaluation Tool!")
            break
        else:
            print("Please enter 'y' for yes or 'n' for no.")

if __name__ == "__main__":
    main()