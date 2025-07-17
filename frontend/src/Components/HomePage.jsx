import { Link } from 'react-router-dom';

const HomePage = () => {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gradient-to-br from-blue-100 to-purple-200 text-center p-8">
      <h1 className="text-4xl font-bold mb-4">Premier League Match Predictor</h1>
      <p className="text-lg mb-6 max-w-xl">
        Get the latest predictions, stats, and insights on upcoming EPL matches.
        Predict match outcomes, view team stats, and compete on the leaderboard!
      </p>
      <div className="flex space-x-4">
        <Link to="/predictions" className="px-6 py-2 bg-blue-600 text-white rounded-full hover:bg-blue-700 transition">Predict Matches</Link>
        <Link to="/leaderboard" className="px-6 py-2 bg-green-600 text-white rounded-full hover:bg-green-700 transition">Leaderboard</Link>
      </div>
    </div>
  );
};

export default HomePage;